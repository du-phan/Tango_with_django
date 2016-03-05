from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'), # matche to an empty string
	url(r'about$', views.about, name='about')	
	) 