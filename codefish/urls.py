from django.conf.urls import patterns, include, url

from codefish.views import home

urlpatterns = patterns('',
    url(r'^$', 'codefish.views.home', name='home'),
)
