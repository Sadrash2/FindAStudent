from django.conf.urls import patterns, url, include

urlpatterns = patterns('accounts.views',
    url(r'^sign_in/$', 'sign_in', name='sign_in'),
    url(r'^sign_up/$', 'sign_up', name='sign_up'),
    url(r'^employer_profile/$', 'employer_profile', name='employer_profile'),
    url(r'^logout_view/$', 'logout_view', name='logout_view'),
    )