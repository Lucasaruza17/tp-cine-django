from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registro/', views.registro, name='registro'),
    path('peliculas/', views.PeliculaList.as_view(), name='pelicula_list'),
    path('peliculas/nueva/', views.PeliculaCreate.as_view(), name='pelicula_create'),
    path('peliculas/<int:pk>/editar/', views.PeliculaUpdate.as_view(), name='pelicula_update'),
    path('peliculas/<int:pk>/eliminar/', views.PeliculaDelete.as_view(), name='pelicula_delete'),
    path('funciones/', views.FuncionList.as_view(), name='funcion_list'),
    path('funciones/nueva/', views.FuncionCreate.as_view(), name='funcion_create'),
    path('funciones/<int:pk>/editar/', views.FuncionUpdate.as_view(), name='funcion_update'),
    path('funciones/<int:pk>/eliminar/', views.FuncionDelete.as_view(), name='funcion_delete'),
    path('funciones/<int:funcion_id>/reservar/', views.reservar_butacas, name='reservar_butacas'),
]