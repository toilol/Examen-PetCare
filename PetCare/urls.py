from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('crud/', views.crud, name='crud'),
    path('editar/<int:servicio_id>/', views.editar, name='editar'),
    path('agregar/', views.agregar, name='agregar'),
    path('borrar/<str:pk>', views.borrar, name='borrar'),
    path('carrito/', views.carrito, name='carrito'),
    path('signin/', views.signin, name='signin'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
]
