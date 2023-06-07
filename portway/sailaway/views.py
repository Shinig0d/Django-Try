from django.shortcuts import render

from.models import Sailaway

# Create your views here.
def index(request):
    return render(request , "sailaway/index.html", {
        "sailaways":Sailaway.objects.all()
    })

def sailaway(request, sailaway_id):
    sailaway = Sailaway.objects.get(pk=sailaway_id)
    return render(request, "sailaway/sailaway.html",{
        "sailaway": sailaway,
        "passengers": sailaway.passengers.all()
    })