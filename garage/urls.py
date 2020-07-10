from django.urls import path
from . import views
from .views import CarListView, CarDetailView, CarCreateView

urlpatterns = [
    path('', CarListView.as_view(), name="garage-home"),
    path('car/new/', CarCreateView.as_view(), name="car-create"),
    path('car/<slug:pk>/', CarDetailView.as_view(), name="car-detail"),
    path('about/', views.about, name="garage-about")
]