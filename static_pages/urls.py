from django.conf.urls import patterns, url, include

urlpatterns = patterns('static_pages.views',
    # url(r'^$', 'overview', name="home"),
    url(r'^$', 'landing_page', name='landing_page'),
)
