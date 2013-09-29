from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'total_photos.views.home', name='home'),
    # url(r'^total_photos/', include('total_photos.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^totalapp/', include('totalapp.urls')),
    url(r'^login/', 'django.contrib.auth.views.login'),
    url(r'^l/', 'login_main_page'),
    url(r'^l/logout/$', 'logout_page'),
)
