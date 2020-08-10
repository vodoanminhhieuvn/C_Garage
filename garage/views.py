#Base django
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django import forms
#Import Class
from .models import Car, Car_Brand, HistoryTrackingCar, Accessories, RepairVote
from .forms import CarUpdateForm


def home(request):
    context = {
        'my_list': Car.objects.all()
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
    # Initialize default value
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

class RepairVoteDetailView(DetailView):
    model = RepairVote
    template_name = 'garage/repairVote_detail.html'

    def get_context_data(self, **kwargs):
        context = super(RepairVoteDetailView, self).get_context_data(**kwargs)
        context['Accessories'] = Accessories.objects.all()
        return context

def about(request):
    return render(request, 'garage/about.html')

def history_home(request):
    context = {
        'my_list': HistoryTrackingCar.objects.all()
    }
    return (request, 'garage/notification.html', context)

class HistoryTrackingCarListView(ListView):
    model = HistoryTrackingCar
    template_name = 'garage/notification.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'my_HistoryTrackingCar'
    paginate_by = 6
    ordering = ['-action_date']
