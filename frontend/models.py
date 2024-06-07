from datetime import timedelta

from django.db import models
from django.utils import timezone

# Create your models here.


class Hall(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=75)
    description = models.TextField()
    capacity = models.IntegerField()
    hourly_rate = models.FloatField()
    region = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    images = models.FileField(upload_to="files/%Y/%m/%d", null=True)

    def __str__(self):
        return f"{self.name}"


class Review(models.Model):
    rating = models.IntegerField()
    author_name = models.CharField(max_length=50)
    author_email = models.EmailField()
    content = models.CharField(max_length=255)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)


class Booking(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    booked_from = models.DateTimeField(default=timezone.now())
    booked_till = models.DateTimeField(default=timezone.now() + timedelta(days=1))
