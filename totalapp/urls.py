from django.conf.urls import patterns, url

from totalapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^homepage$', views.homepage, name='homepage'),
    url(r'^album/(?P<album_id>\d+)/$', views.album, name='album'),
)