# -*- coding:utf-8 -*-  
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,render
#from django.db import models 
from jythink.models import Message, User1
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.contrib import auth
from django.contrib.auth import authenticate, login
import pdb

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

#注册
class UserForm(forms.Form): 
    email  = forms.EmailField(label='email',widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"请输入邮箱账号", "value": "", "required": "required",}), max_length=100, error_messages={"required": "用户名不能为空",})
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "请输入密码", "value": "", "required": "required",}), min_length=8, max_length=50,error_messages={"required": "密码不能为空",})

    def clean(self):  
         # 用户名  
        try:            
            username=self.cleaned_data['email']  
        except Exception as e:  
            print 'except: '+ str(e)  
            raise forms.ValidationError(u"注册账号需为邮箱格式")      
  
        # 登录验证          
        is_email_exist = User1.objects.filter(email=username).exists()   
        is_username_exist = User1.objects.filter(username=username).exists()   
        if is_username_exist or is_email_exist:  
            raise forms.ValidationError(u"该账号已被注册")  
  
        # 密码  
        try:  
            password=self.cleaned_data['password']  
        except Exception as e:  
            print 'except: '+ str(e)  
            raise forms.ValidationError(u"请输入至少8位密码");  
  
        return self.cleaned_data 

# 获取表单提示信息  
def getFormTips(form):  
    errors = form._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())  
    err = errors.pop()   
    if err:  
        print type(err)  
        if isinstance(err, str):  
            print 'str'  
        else:  
            err = err.message  
    print err  
    return err 

def setFormTips(form, content):   
    if content and len(content)>0:   
        errors = form._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())  
        errors.append(content) 

@csrf_exempt
def register(request):
    pdb.set_trace()
    if request.method == 'POST':
        try:
            uf = UserForm(request.POST)
        except Exception as e:  
            print str(e)  
            # 登录失败 返回错误提示      
            err = "注册失败，请重试"  
            return result_response(request, err) 

        if uf.is_valid():
            try:  
                #获得表单数据
                username = uf.cleaned_data['email']
                password = uf.cleaned_data['password']
                #添加到数据库
                user = User1.objects.create(username = username, email = username, password = password) 
                user.save()  
                user.backend = 'django.contrib.auth.backends.ModelBackend' # 指定默认的登录验证方式  
                # 验证成功登录  
                #auth.login(request, user)  
                return render_to_response('index.html', context = {'uf': "OK"})
            except Exception as e:  
                print str(e)  
                setFormTips(uf, "注册失败，请重试")  
        else:  
            print "register failed"  
  
            if request.POST.get('captcha_v') == "":  
                setFormTips(uf, "验证码不能为空")   
  
        # 登录失败 返回错误提示      
        err = getFormTips(uf)  
        return render_to_response('index.html', context = {'uf': err})
    else:
        uf = UserForm()
    return render_to_response('index.html',context = {'uf':uf})

#登录
class UserFormLogin(forms.Form):
    login = forms.EmailField(label='email',widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"请输入邮箱账号", "value": "", "required": "required",}), max_length=100, error_messages={"required": "用户名不能为空",})
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "请输入密码", "value": "", "required": "required",}), min_length=8, max_length=50,error_messages={"required": "密码不能为空",})

@csrf_exempt
def login(request):
    pdb.set_trace()
    if request.method == 'POST':
        uf = UserFormLogin(request.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['login']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User1.objects.filter(username__exact = username,password__exact = password)
            if user is not None:
                #比较成功，跳转index
                response = HttpResponseRedirect('/online/index/')
                #将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username',username,3600)
                return response
            else:
                #比较失败，还在login
                return HttpResponseRedirect('/online/login/')
    else:
        uf = UserFormLogin()
        print "login failed"
        return render(request, 'index.html', context = "error")

