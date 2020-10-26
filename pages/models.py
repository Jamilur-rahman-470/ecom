from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length= 40)
    message = models.TextField()

    def __str__(self):
        return self.email