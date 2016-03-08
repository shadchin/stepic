from django.conf.urls import url

from qa.views import test, question, main, popular, ask, answer

urlpatterns = [
    url(r'^$', main),
    url(r'^login/$', test),
    url(r'^signup/$', test),
    url(r'^question/(?P<id>[^/]+)/$', question, name='question'),
    url(r'^ask/$', ask),
    url(r'^answer/$', answer),
    url(r'^popular/$', popular),
    url(r'^new/$', test),
]
