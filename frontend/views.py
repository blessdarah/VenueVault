from django.contrib import messages
from django.shortcuts import render

from .forms import BookingRequestForm
from .models import Hall


def signup(request):
    if request.method == "POST":
        pass
    return render(request, "frontend/signup.html")


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
    try:
        hall = Hall.objects.get(pk=hall_id)
        form = BookingRequestForm()
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
        return render(request, "frontend/booking.html", {"hall": hall, "form": form})
    except Hall.DoesNotExist:
        return render(request, "frontend/404.html")
