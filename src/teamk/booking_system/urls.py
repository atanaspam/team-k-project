from django.conf.urls import patterns, url
from booking_system import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'))
