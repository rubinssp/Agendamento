from django.urls import path
from .views import ClientespfView, ClientepfAddView, ClientepfUpDateView, ClientepfDeleteView

urlpatterns = [
    path('clientespf', ClientespfView.as_view(), name='clientespf'),
    path('clientepf/adicionar/', ClientepfAddView.as_view(), name='clientepf_adicionar'),
    path('<int:pk>/clientepf/editar/', ClientepfUpDateView.as_view(), name='clientepf_editar'),
    path('<int:pk>/clientepf/apagar/', ClientepfDeleteView.as_view(), name='clientepf_apagar'),

]