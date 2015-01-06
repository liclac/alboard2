from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from booru.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'alboard2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^event/new/$', PoolCreateView.as_view(), name='pool-new'),
    url(r'^event/(?P<pk>\d+)/$', PoolView.as_view(), name='pool'),
    url(r'^event/(?P<pk>\d+)/edit/$', PoolUpdateView.as_view(), name='pool-edit'),
    url(r'^event/(?P<pid>\d+)/upload/$', PostCreateView.as_view(), name='upload'),
    url(r'^event/(?P<pid>\d+)/(?P<pk>\d+)/$', PostView.as_view(), name='post'),
    url(r'^event/(?P<pid>\d+)/(?P<pk>\d+)/edit/$', PostUpdateView.as_view(), name='post-edit'),
    
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
    )
