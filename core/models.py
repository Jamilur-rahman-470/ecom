from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# User Profile Model
class AddressAndInfo(models.Model):
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    home_street = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)
    user = models.ForeignKey(to=User, unique=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'

class Profile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    info =models.ForeignKey(to=AddressAndInfo, unique=True, on_delete=models.CASCADE)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.first_name}'