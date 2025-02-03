from django.urls import path
from . import views

urlpatterns = [
    path('api/info/', views.get_info, name='get_info'),
]
