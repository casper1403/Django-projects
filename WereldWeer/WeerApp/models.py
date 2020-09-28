from django.db import models

# Create your models here.
class City(models.Model):

    name = models.CharField(max_length = 60)
    country = models.CharField(max_length = 40)
    subcountry = models.CharField(max_length = 40, null=True)
    geonameid = models.CharField(max_length = 40)


    def __str__(self):
        return self.name
