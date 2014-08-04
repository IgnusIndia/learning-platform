from django.conf.urls import patterns, include, url

from views import ConceptListView, ConceptDetailView

urlpatterns = patterns('',
    
    
    url(r'^browse/', ConceptListView.as_view()),
    url(r'^browse/(?P<slug>[-_\w]+)/$', ConceptDetailView.as_view(), name='concept-detail'),
    
)
