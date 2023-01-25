from django.urls import path
from .views import VeiculosView

urlpatterns = [
    path('veiculos', VeiculosView.as_view(), name='veiculos'),
]