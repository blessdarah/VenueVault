from datetime import timedelta
from enum import Enum

from django.db import models
from django.utils import timezone


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


class Perk(models.Model):
    perk = models.CharField(max_length=100)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)


class Status(Enum):
    APPROVED = "Approved"
    REJECTED = "Rejected"
    CREATED = "Created"


class Booking(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    booked_from = models.DateTimeField(default=timezone.now())
    booked_till = models.DateTimeField(default=timezone.now() + timedelta(days=1))
    status = models.CharField(
        max_length=15,
        choices=[(tag.name, tag.value) for tag in Status],
        default=Status.CREATED.value,
    )


class BookingRequest(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    booked_from = models.DateTimeField(default=timezone.now())
    booked_till = models.DateTimeField(default=timezone.now() + timedelta(days=1))
    status = models.CharField(
        max_length=15,
        choices=[(tag.name, tag.value) for tag in Status],
        default=Status.CREATED.value,
    )
    customer_name = models.CharField(max_length=70)
    customer_email = models.EmailField()
    customer_address = models.CharField(max_length=60)
    customer_contact = models.CharField(max_length=15)
