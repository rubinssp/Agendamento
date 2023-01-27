from django.urls import path
from .views import ClientespjView, ClientepjAddView, ClientepjUpDateView, ClientepjDeleteView

urlpatterns = [
    path('clientespj', ClientespjView.as_view(), name='clientespj'),
    path('clientepj/adicionar/', ClientepjAddView.as_view(), name='clientepj_adicionar'),
    path('<int:pk>/clientepj/editar/', ClientepjUpDateView.as_view(), name='clientepj_editar'),
    path('<int:pk>/clientepj/apagar/', ClientepjDeleteView.as_view(), name='clientepj_apagar'),

]