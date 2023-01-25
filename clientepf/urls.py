from django.urls import path
from .views import ClientespfView

urlpatterns = [
    path('clientespf', ClientespfView.as_view(), name='clientespf'),
]