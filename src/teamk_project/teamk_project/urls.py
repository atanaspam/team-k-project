from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'teamk_project.views.home', name='home'),
    # url(r'^teamk_project/', include('teamk_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^bookingsystem/', include('bookingsystem.urls')),
    url(r'^$', 'teamk_project.views.login', name='login'),
    url(r'^login_view/', 'teamk_project.views.login_view', name='login_view'),
    url(r'^register/', 'teamk_project.views.register', name='register'),
)
