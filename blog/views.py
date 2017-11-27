# -*- coding:utf-8 -*-
import markdown
import sys
from django.shortcuts import render, get_object_or_404
from comments.form import CommentForm
from .models import Post, Category, Typecho_Posts
reload(sys)
sys.setdefaultencoding('UTF8')

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

    print type(post.text)

    dest = post.text.decode('string_escape')

    print type(dest)
    post.text = markdown.markdown(dest,
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
