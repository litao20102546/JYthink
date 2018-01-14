# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def classes(request):
     return render(request, 'class.html')

def show(request):
     return render(request, 'show.html')
