from django import forms
from .models import Car, Car_Brand
from .forms import CarUpdateForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


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
    paginate_by = 6

class UserCarListView(ListView):
    model = Car
    template_name = 'garage/user_home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'my_list'
    paginate_by = 6

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Car.objects.filter(staff=user).order_by('-date_received')

class CarDetailView(DetailView):
    model = Car

class CarCreateView(LoginRequiredMixin, CreateView):
    model = Car
    fields = ['owner', 'address', 'license_plate', 'phone_number', 'email', 'car_brand', 'fee']

    def form_valid(self, form):
        form.instance.staff = self.request.user
        return super().form_valid(form)


class CarUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Car
    is_edited = forms.BooleanField(disabled=True)
    form_class = CarUpdateForm
    def form_valid(self, form):
        form.instance.staff = self.request.user
        return super().form_valid(form)

    def test_func(self):
        Car = self.get_object()
        if self.request.user.is_superuser:
            return True
        return False
    
    def get_initial(self):
        return {'is_edited': True}


class CarDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Car
    success_url = '/'
    
    def test_func(self):
        Car = self.get_object()
        if self.request.user.is_superuser:
            return True
        return False

def about(request):
    return render(request, 'garage/about.html')