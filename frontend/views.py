from django.shortcuts import render

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
