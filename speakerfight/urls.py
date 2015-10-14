from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/', include('allauth.urls')),

    url(r'^', include('core.urls')),
    url(r'^', include('deck.urls')),
    url(r'^', include('jury.urls')),
    url(r'^api/', include('api.urls')),
)
