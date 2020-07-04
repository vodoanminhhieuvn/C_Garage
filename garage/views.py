from django.shortcuts import render
from .models import Car, Car_Brand


def home(request):
    my_list = Car.objects.all()
    context = {
        'my_list': my_list
    }
    return render(request, 'garage/home.html', context)

def about(request):
    return render(request, 'garage/about.html')