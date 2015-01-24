from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from booru.views import *
from .views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'alboard2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', PostsView.as_view(), name='posts'),
    url(r'^upload/$', PostCreateView.as_view(), name='upload'),
    url(r'^event/new/$', PoolCreateView.as_view(), name='pool-new'),
    url(r'^event/(?P<pk>\d+)/$', PoolView.as_view(), name='pool'),
    url(r'^event/(?P<pk>\d+)/edit/$', PoolUpdateView.as_view(), name='pool-edit'),
    url(r'^event/(?P<pid>\d+)/upload/$', PostCreateView.as_view(), name='pool-upload'),
    url(r'^event/(?P<pid>\d+)/(?P<pk>\d+)/$', PostView.as_view(), name='post'),
    url(r'^event/(?P<pid>\d+)/(?P<pk>\d+)/edit/$', PostUpdateView.as_view(), name='post-edit'),
    
    url(r'^accounts/profile/$', ProfileUpdateView.as_view(), name='account_profile'),
    url(r'^accounts/delete/$', ProfileDeleteView.as_view(), name='account_delete'),
    url(r'^accounts/login/$', TemplateView.as_view(template_name='account/login.html'), name='account_login'),
    url(r'^accounts/login/local/$', 'django.contrib.auth.views.login', {'template_name': 'account/login_local.html'}, name='account_login_local'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='account_logout'),
    url(r'^accounts/', include('social.apps.django_app.urls', namespace='social')),
    
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
    )

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
