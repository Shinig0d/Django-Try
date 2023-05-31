from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("shini", views.shini, name="shini"),
    path("<str:name>", views.greet, name="greet")
]