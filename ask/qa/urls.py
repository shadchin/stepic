from django.conf.urls import url

from qa.views import test, question, main, popular

urlpatterns = [
    url(r'^$', main),
    url(r'^login/$', test),
    url(r'^signup/$', test),
    url(r'^question/(?P<id>[^/]+)/$', question, name='question'),
    url(r'^ask', test),
    url(r'^popular/$', popular),
    url(r'^new/$', test),
]
