from django.urls import path
from . import views

urlpatterns = [
    path('classify-number', views.get_number, name='get_number'),
]
