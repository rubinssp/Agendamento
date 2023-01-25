from django.urls import path
from .views import VagasView

urlpatterns = [
    path('vagas', VagasView.as_view(), name='vagas'),
]