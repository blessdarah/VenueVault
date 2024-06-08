from django.contrib import messages
from django.shortcuts import render

from .forms import BookingRequestForm
from .models import Hall


def index(request):
    halls = Hall.objects.all()
    return render(request, "frontend/index.html", {"halls": halls})


def show_hall(request, hall_id):
    hall = Hall.objects.get(pk=hall_id)
    print(hall)
    return render(
        request,
        "frontend/hall.html",
        {
            "hall": hall,
        },
    )


def book_request(request, hall_id):
    hall = Hall.objects.get(pk=hall_id)
    if request.method == "POST":
        form = BookingRequestForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.hall_id = hall_id
            instance.save()
            form = BookingRequestForm()
            messages.add_message(
                request, messages.INFO, "Your request has been sent successfully"
            )
        else:
            form = BookingRequestForm()
    return render(request, "frontend/booking.html", {"hall": hall, "form": form})
