from django.conf.urls import patterns, include, url
import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'', include('static_pages.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
