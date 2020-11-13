from . import views
from django.urls import path


urlpatterns = [
    path('', views.index),
    path('send_renta', views.send_renta),
    path('send_money', views.send_money),
]
