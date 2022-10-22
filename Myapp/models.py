from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=15)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
