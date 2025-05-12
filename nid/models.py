from django.db import models
from users.models import User


class NID(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='nids', unique=True)
    nid = models.CharField(max_length=20, unique=True)
    photo = models.ImageField(upload_to='nid_photos/')

    class Meta:
        unique_together = ('user', 'nid')

    def __str__(self):
        return f"{self.user.email} - {self.nid}"
