from django.contrib import admin
from .models import Post, Category, Tag,Typecho_Posts


class PostAdmin(admin.ModelAdmin):
    list_display = ['title','commentsNum','views']

admin.site.register(Typecho_Posts,PostAdmin)
