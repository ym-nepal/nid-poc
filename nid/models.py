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
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    nid = models.ForeignKey("nid.NID", on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="nid_photos")

    def __str__(self):
        return f"{self.user} - {self.nid}"