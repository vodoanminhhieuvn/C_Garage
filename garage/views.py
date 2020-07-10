from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Car, Car_Brand
from django.views.generic import ListView, DetailView, CreateView


def home(request):
    my_list = Car.objects.all()
    context = {
        'my_list': my_list
    }
    return render(request, 'garage/home.html', context)

#class help us to easily control what we want user to see
class CarListView(ListView):
    model = Car
    template_name = 'garage/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'my_list'
    ordering = ['-date_received']

class CarDetailView(DetailView):
    model = Car

class CarCreateView(LoginRequiredMixin, CreateView):
    model = Car
    fields = ['car_id', 'owner', 'address', 'license_plate', 'phone_number', 'email', 'car_brand']

    def form_valid(self, form):
        form.instance.staff = self.request.user
        return super().form_valid(form)

def about(request):
    return render(request, 'garage/about.html')