from tastypie import fields
from tastypie.resources import ModelResource
from gal.models import Image, Gallery


class GalleryResource(ModelResource):
    class Meta:
        queryset = Gallery.objects.all()
        allowed_methods = ['get']


class ImageResource(ModelResource):
    gallery = fields.ForeignKey(GalleryResource, 'gallery')

    class Meta:
        queryset = Image.objects.all()
        allowed_methods = ['get']
