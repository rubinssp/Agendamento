from django.urls import path
from .views import ClientespjView

urlpatterns = [
    path('clientespj', ClientespjView.as_view(), name='clientespj'),
]