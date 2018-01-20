from django.conf.urls import include, url
from question import views

 
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^article', views.article),
    url(r'^test', views.test ,name = 'test'),
]
