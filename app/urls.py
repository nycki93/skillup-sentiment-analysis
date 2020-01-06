from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('parrot/<str:query>', views.parrot, name='parrot'),
]