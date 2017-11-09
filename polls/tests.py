# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question

# Create your tests here.

def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days = days)
    return Question.objects.create(question_text = question_text, pub_date = time)

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date = time)
        self.assertIs(future_question.was_published_recently(),False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1,seconds = 1)
        future_question = Question(pub_date = time)
        self.assertIs(future_question.was_published_recently(),False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours = 23,minutes = 59,seconds = 59)
        future_question = Question(pub_date = time)
        self.assertIs(future_question.was_published_recently(),True)

# todo: https://docs.djangoproject.com/en/1.11/intro/tutorial05/#testing-our-new-view