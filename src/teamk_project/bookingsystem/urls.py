from django.conf.urls import patterns, url
from bookingsystem import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^sessions', views.sessions, name ='sessions'),
	url(r'^editProfile', views.editProfile, name='editProfile'))
