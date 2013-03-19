from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from tastypie.api import Api
from galsite.api.resources import ImageResource, GalleryResource

v1_api = Api(api_name='v1')
v1_api.register(ImageResource())
v1_api.register(GalleryResource())

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    (r'^api/', include(v1_api.urls)),

    url(r'^', include('gal.urls')),
)
