from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.auth import views as auth_views
admin.autodiscover()

from tastypie.api import Api
from proofs.api.resources import ImageResource, GalleryResource

v1_api = Api(api_name='v1')
v1_api.register(ImageResource())
v1_api.register(GalleryResource())

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^login/?$',
        auth_views.login,
        {'template_name': 'login.html'},
        name='auth_login'),
    url(r'^logout/?$',
        auth_views.logout,
        {'template_name': 'logout.html'},
        name='auth_logout'),

    (r'^api/', include(v1_api.urls)),

    url(r'^(?P<gallery>[^/]+)$', 'proofs.views.index'),
    url(r'^$', 'proofs.views.home'),

    url(r'^', include('gal.urls')),
)
