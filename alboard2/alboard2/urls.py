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
    
    url(r'^event/(?P<pk>\d+)/$', PoolView.as_view(), name='pool'),
    url(r'^event/(\d+)/(?P<pk>\d+)/$', PostView.as_view(), name='post'),
    
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
    )
