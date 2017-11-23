from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible
import time

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=70)

    body = models.TextField()

    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    excerpt = models.CharField(max_length=200, blank=True)

    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    author = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_time']

class Typecho_Posts(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)

    created_time = models.IntegerField()
    modified_time = models.IntegerField()

    text = models.TextField()

    commentsNum = models.IntegerField(blank=True)
    allowComment = models.CharField(max_length=255, blank=True, default='0')
    views = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def get_created_time(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.created_time))

    class Meta:
        ordering = ['-created_time']
