from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('crud/', views.crud, name='crud'),
    path('editar/<int:servicio_id>/', views.editar, name='editar'),
    path('agregar/', views.agregar, name='agregar'),
    path('borrar/<str:pk>', views.borrar, name='borrar'),
    path('carrito/', views.carrito, name='carrito'),
    
]
