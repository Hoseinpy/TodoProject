from django.urls import path
from .views import AddApiView, DetailApiView


urlpatterns = [
    path('add/', AddApiView.as_view(), name='add-api'),
    path('detail/', DetailApiView.as_view(), name='detai-api'),
]
