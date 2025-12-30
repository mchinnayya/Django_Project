from django.db import models

# Create your models here.

class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    query = models.TextField(max_length=500)

    def __str__(self):
        return self.name
