from django.db import models

# Create your models here.
from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    country = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Rate(models.Model):
    rate = models.IntegerField(default=0)
    review = models.CharField(max_length=300)
    place = models.ForeignKey('Place', on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.place, self.rate)
