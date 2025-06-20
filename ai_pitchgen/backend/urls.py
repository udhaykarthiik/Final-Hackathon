from django.urls import path
from .views import generate_pitch

urlpatterns = [
    path('api/generate-pitch/', generate_pitch, name='generate-pitch'),
]