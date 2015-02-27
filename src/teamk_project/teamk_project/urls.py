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
    url(r'^register', 'teamk_project.views.register', name='register'),
    url(r'^logout/', 'teamk_project.views.logout', name='logout'),
    url(r'^invalid', 'teamk_project.views.invalid', name='invalid'),
    url(r'^fail', 'teamk_project.views.fail', name='fail'),
    url(r'^success', 'teamk_project.views.success', name='success'),
    url(r'^successEmb', 'teamk_project.views.successEmb', name='successEmb'),
    url(r'^editProfile', 'teamk_project.views.editProfile', name='editProfile'),
    url(r'^changePassword','teamk_project.views.changePassword', name='changePassword')
)
