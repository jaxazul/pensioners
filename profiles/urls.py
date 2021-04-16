from django.urls import path

from . import views

urlpatterns = [
    # path('technician', views.technician, name='technician'),
    path('', views.index, name='profile'),
]