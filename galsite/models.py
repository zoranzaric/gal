from django.db import models

from django.contrib.auth.models import User
from gal.models import Gallery

class UserCanAccessGallery(models.Model):
    user = models.ForeignKey(User)
    gallery = models.ForeignKey(Gallery)

