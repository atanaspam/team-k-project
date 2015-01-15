from django.conf.urls import patterns, url
from coach import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^index', views.index, name='index'),
	url(r'^sessions', views.sessions, name='sessions'),
	url(r'^attendance', views.attendance, name='attendance'),
	url(r'^editProfile', views.editProfile, name='editProfile'))
