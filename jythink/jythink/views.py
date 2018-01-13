
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,render
#from django.db import models 
from jythink.models import Message

def test(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        print username
        password = request.POST.get("password", None)
        #Message.objects.create(username=username, password=password)
        M = Message(username=username, password=password)
        M.save()
        print "ok"
    return render(request, 'test.html') 

#Bootstrap test
def index(request):
     return render(request, 'index.html')

def register(request):
     return render(request, 'register.html')

def login(request):
     return render(request, 'login.html')

def coding(request):
     return render(request, 'coding.html')

def contact(request):
     return render(request, 'contact.html')

def question(request):
     return render(request, 'question.html')

def classes(request):
     return render(request, 'class.html')

def show(request):
     return render(request, 'show.html')

def news(request):
     return render(request, 'news.html')

def article(request):
     return render(request, 'article.html')
