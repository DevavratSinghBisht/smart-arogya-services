from django.urls import path
from . import views

urlpatterns = [
    path('diagnosis', views.diagnosis, name='diagnosis')
]