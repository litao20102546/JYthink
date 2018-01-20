# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
     return render(request, 'question-index.html')

def test(request):
     return render(request, 'test.html')

def article(request):
     return render(request, 'article.html')
