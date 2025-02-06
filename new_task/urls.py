from django.urls import path
from . import views

urlpatterns = [
    path('api/classify-number', views.get_number, name='get_number'),
]
