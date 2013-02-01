from django.conf.urls import patterns, include, url
import settings
from kursoapp.views import ingresar, salir
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kurso.views.home', name='home'),
    url(r'^kurso/', include('kursoapp.urls')),
    url(r'^salir/$', salir),
    url(r'^ingresar/$', ingresar),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

)
