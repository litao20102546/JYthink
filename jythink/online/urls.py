from django.conf.urls import include, url
from online import views

 
urlpatterns = [
    url(r'^$', views.login, name='login1'),
    url(r'^log', views.login,name = 'login1'),
    url(r'^test', views.test, name = 'test'),
    url(r'^regist/$',views.regist,name = 'regist'),
    url(r'^index',views.index,name = 'index'),
    url(r'^logout/$',views.logout,name = 'logout'),
]
