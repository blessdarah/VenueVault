from django.contrib import admin

from .models import Booking, BookingRequest, Hall, Perk, Review

# Register your models here.


@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "address",
        "description",
        "hourly_rate",
        "region",
        "city",
    ]


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = [
        "hall",
        "booked_from",
        "booked_till",
    ]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = [
        "hall",
        "rating",
        "content",
        "author_name",
        "author_email",
    ]


@admin.register(Perk)
class PerkAdmin(admin.ModelAdmin):
    list_display = [
        "perk",
    ]


@admin.register(BookingRequest)
class BookingRequstAdmin(admin.ModelAdmin):
    list_display = [
        "hall",
        "booked_from",
        "booked_till",
        "status",
        "customer_name",
        "customer_email",
        "customer_address",
        "customer_contact",
    ]
