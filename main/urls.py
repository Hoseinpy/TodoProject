from django.urls import path
from .views import AddApiView, DetailApiView, StatsApiView


urlpatterns = [
    path('todo/', AddApiView.as_view(), name='add-api'),
    path('todo/<int:pk>', DetailApiView.as_view(), name='detail-api'),
    path('stats/', StatsApiView.as_view(), name='stats-api')
]
