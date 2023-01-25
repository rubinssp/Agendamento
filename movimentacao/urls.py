from django.urls import path
from .views import MovimentacoesView

urlpatterns = [
    path('movimentacoes', MovimentacoesView.as_view(), name='movimentacoes'),
]