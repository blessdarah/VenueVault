from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path("/", views.index, name="index"),
    path("", views.index, name="index"),
    path("halls/<int:hall_id>", views.show_hall),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
