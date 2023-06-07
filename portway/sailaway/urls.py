from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:sailaway_id>", views.sailaway, name="sailaway")
]