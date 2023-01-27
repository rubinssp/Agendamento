from django.urls import path
from .views import MovimentacoesView, MovimentacaoAddView, MovimentacaoUpDateView, MovimentacaoDeleteView

urlpatterns = [
    path('movimentacoes', MovimentacoesView.as_view(), name='movimentacoes'),
    path('movimentacao/adicionar/', MovimentacaoAddView.as_view(), name='movimentacao_adicionar'),
    path('<int:pk>/movimentacao/editar/', MovimentacaoUpDateView.as_view(), name='movimentacao_editar'),
    path('<int:pk>/movimentacao/apagar/', MovimentacaoDeleteView.as_view(), name='movimentacao_apagar'),
]