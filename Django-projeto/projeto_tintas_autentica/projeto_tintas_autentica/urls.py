from django.urls import path
from app_cad_tintas import views

urlpatterns = [
    path('',views.home,name='home'),
    path('tintas/', views.tintas,name='lista_de_tintas')
]
