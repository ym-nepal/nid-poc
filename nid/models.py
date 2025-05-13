from django.db import models


class NID(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    nid = models.BigIntegerField(unique=True)
    fullname = models.CharField(max_length=255)
    dob = models.DateField(verbose_name="Date of Birth")
    address = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return f"{self.fullname} - {self.nid}"


class NIDUser(models.Model):
    nid = models.BigIntegerField()
    photo = models.ImageField(upload_to="nid_photos")

    def __str__(self):
        return f"{self.user} - {self.nid}"