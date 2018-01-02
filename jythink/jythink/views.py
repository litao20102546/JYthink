
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,render
 
def hello(request):
    return HttpResponse("Hello world ! ")

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
