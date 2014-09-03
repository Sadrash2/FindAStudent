from django.conf.urls import patterns, url, include

urlpatterns = patterns('employer.views',
    url(r'^post_job/$', 'post_job', name='post_job'),
    url(r'^manage_jobs/$', 'manage_jobs', name='manage_jobs'),
    url(r'^employer_profile/$', 'employer_profile', name='employer_profile'),
    )