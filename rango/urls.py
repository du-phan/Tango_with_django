from django.conf.urls import url
from rango import views

urlpatterns = [
	url(r'^$', views.index, name='index'), # matche to an empty string
	url(r'^about', views.about, name='about')	
]