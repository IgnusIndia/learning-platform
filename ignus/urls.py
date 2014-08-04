from django.conf.urls import patterns, include, url

from django.views.generic import ListView, DetailView

from concept.views import ConceptListView, ConceptDetailView
from concept.models import Concept

from django.contrib import admin
admin.autodiscover()

from concept import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'concepts', views.ConceptViewSet)

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'profiles.views.index', name='index'),
    url(r'^api/', include(router.urls)),
    url(r'^browse/', ConceptListView.as_view()),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^(?P<slug>[-_\w]+)/$', ConceptDetailView.as_view(), name='concept-detail'),
    #url(r'^$concepts', views.concepts_gallery, name='concepts_gallery'),
    # url(r'^blog/', include('blog.urls')),
    
    

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
     {'next_page': '/'}),

)








