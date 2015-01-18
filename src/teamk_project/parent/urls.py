from django.conf.urls import patterns, url
from parent import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^index', views.index, name='index'),
	url(r'^bookings', views.bookings, name='bookings'),
	url(r'^childrenList', views.childrenList, name='childrenList'),
	url(r'^childProfile', views.childProfile, name='childProfile'),
	url(r'^addNewChild', views.addNewChild, name='addNewChild'),
	url(r'^payments', views.payments, name='payments'),
	url(r'^editProfile', views.editProfile, name='editProfile'))