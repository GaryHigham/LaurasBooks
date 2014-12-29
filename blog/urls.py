from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views

urlpatterns = [
    url(r'^blogentries/$', views.BlogList.as_view()),
    url(r'^blogentries/(?P<pk>[0-9]+)/$', views.BlogDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)