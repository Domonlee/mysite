# -*- coding:utf-8 -*-
import markdown

from django.shortcuts import render, get_object_or_404
from comments.form import CommentForm
from .models import Post, Category, Typecho_Posts


def index(request):
    post_list = Typecho_Posts.objects.all().order_by('-created_time')

    return render(request, 'blog/index.html', context={'post_list': post_list})


def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def detail(request, pk):
    post = get_object_or_404(Typecho_Posts, pk=pk)
    # test began
    str = post.text.encode('utf-8')
    print str
    # print str.decode('unicode_escape')
    print post.text.encode('unicode_escape')
    print '=-=-='
    text = '<!--markdown-->今天在Youtube上看一个视频教程的时候，才知道Python下面有这样一个好东西，有点类似Docker，实际上又比Docker轻量级很多。Python的优点就是库很多，很方便的站在别人肩膀上快速开发。但这个有点也是一个缺点，在项目比较多的情况下，由于所有的**site-packages**都是公用的，这样不便于修改配置。所以，需要有一个类似虚拟环境的东西，来保证对于单个项目中的虚拟环境都是互相隔离的，特别的纯净。\r\n\r\n安装的过程实际上也特别的简单:\r\n> pip install virtualenv\r\n\r\n'
    print text
    print '=-=-='

    # test end

    post.text = markdown.markdown(post.text,
                                  extensions=[
                                      'markdown.extensions.nl2br',
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    form = CommentForm()

    context = {
        'post': post,
        'form': form,
    }

    return render(request, 'blog/detail.html', context=context)
