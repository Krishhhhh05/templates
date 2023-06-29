from django.shortcuts import render
from .models import Person
# Create your views here.
def homePage(request):
    return render(request, "index.html")

def first(request):
    return render(request, "first.html")
def all_data(request):
    data=Person.objects.all()
    return render(request, "data.html",{'data':data})

    pass