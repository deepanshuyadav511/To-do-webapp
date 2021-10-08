from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "home"),
    path('delete/<str:pk>', views.delete, name='delete'),
]
