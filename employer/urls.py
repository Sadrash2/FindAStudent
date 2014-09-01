from django.conf.urls import patterns, url, include

urlpatterns = patterns('employer.views',
    url(r'^post_job/$', 'post_job', name='post_job'),
    )