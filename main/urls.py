from django.urls import path
from .views import AddApiView, DetailApiView, StatsApiView, List_Todo


urlpatterns = [
    path('todo/add/', AddApiView.as_view(), name='add-api'),
    path('todo/<int:pk>', DetailApiView.as_view(), name='detail-api'),
    path('stats/', StatsApiView.as_view(), name='stats-api'),
    path('todo/', List_Todo.as_view(), name='list-api'),
]
