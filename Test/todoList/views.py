from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

tasks = ["Do Hw", "Dance"]

# Create your views here.
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "todoList/index.html", {
        "tasks":request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("todoList:index"))
        else:
            return render(request, "todoList/add.html", {
                "form": form
            })
    return render(request, "todoList/add.html", {
        "form":NewTaskForm()
    })