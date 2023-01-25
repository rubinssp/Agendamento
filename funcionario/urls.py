from django.urls import path
from .views import FuncionariosView

urlpatterns = [
    path('funcionarios', FuncionariosView.as_view(), name='funcionarios'),
]