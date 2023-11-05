from django.urls import path, include
from . import views

urlpatterns = [
    path('nuevo-usuario/', views.nuevo_usuario, name='nuevo_usuario'),
    path('nuevo-tema/', views.nuevo_tema, name='nuevo_tema'),
    path('nueva-discusion/', views.nueva_discusion, name='nueva_discusion'),
    path('buscar/', views.buscar, name='buscar'),
    path('iniciar-sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    #path("blog/", include("blog.urls")),
]