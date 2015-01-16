from django.conf.urls import patterns, url
from manager import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^index', views.index, name='index'),
	url(r'^bookings', views.bookings, name='bookings'),
	url(r'^coaches', views.coaches, name='coaches')
)