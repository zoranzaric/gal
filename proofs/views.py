from gal import views as galviews
from gal.models import Gallery
from proofs.models import UserCanAccessGallery
from django.core.exceptions import PermissionDenied
from django.shortcuts import render_to_response, get_object_or_404, redirect


def home (request):
    if request.user.is_authenticated():
        galleries = [ucag.gallery.name
                     for ucag
                     in UserCanAccessGallery.objects.filter(user=request.user)]
        return render_to_response('home.html', {'galleries': sorted(galleries)})
    else:
        return redirect('auth_login')


def index(request, gallery):
    if request.user.is_authenticated():
        gallery = get_object_or_404(Gallery, name=gallery)
        try:
            UserCanAccessGallery.objects.get(user=request.user, gallery=gallery)
        except UserCanAccessGallery.DoesNotExist:
            raise PermissionDenied
    else:
        raise PermissionDenied
    return galviews.index(request, gallery)

