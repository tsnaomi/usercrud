from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'usercrud.views.home', name='home'),
    # url(r'^usercrud/', include('usercrud.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^users/$', 'usercrud.usertracker.views.list'),

    url(r'^users/(?P<page>\d+)', 'usercrud.usertracker.views.list'),

    url(r'^users/new', 'usercrud.usertracker.views.new'),

    url(r'^users/add', 'usercrud.usertracker.views.add'),

    url(r'^users/edit/(?P<id>\d+)', 'usercrud.usertracker.views.edit'),

    url(r'^users/update/(?P<id>\d+)', 'usercrud.usertracker.views.update'),

    url(r'^users/delete/(?P<id>\d+)', 'usercrud.usertracker.views.delete')
)