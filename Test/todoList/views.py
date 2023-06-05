from django import forms
from django.shortcuts import render

tasks = ["Do Hw", "Dance"]

# Create your views here.


def index(request):
    return render(request, "todoList/index.html", {
        "tasks":tasks
    })

def add(request):
    return render(request, "todoList/add.html")