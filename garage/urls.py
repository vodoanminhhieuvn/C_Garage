from django.urls import path
from . import views
from .views import CarListView, CarDetailView, CarCreateView, CarUpdateView, CarDeleteView

urlpatterns = [
    path('', CarListView.as_view(), name="garage-home"),
    path('car/new/', CarCreateView.as_view(), name="car-create"),
    path('car/<slug:pk>/', CarDetailView.as_view(), name="car-detail"),
    path('car/<slug:pk>/update', CarUpdateView.as_view(), name="car-update"),
    path('car/<slug:pk>/delete', CarDeleteView.as_view(), name="car-delete"),
    path('about/', views.about, name="garage-about")
]