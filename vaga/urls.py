from django.urls import path
from .views import VagasView, VagaAddView, VagaUpDateView, VagaDeleteView

urlpatterns = [
    path('vagas', VagasView.as_view(), name='vagas'),
    path('vaga/adicionar/', VagaAddView.as_view(), name='vaga_adicionar'),
    path('<int:pk>/vaga/editar/', VagaUpDateView.as_view(), name='vaga_editar'),
    path('<int:pk>/vaga/apagar/', VagaDeleteView.as_view(), name='vaga_apagar'),
]