from django.urls import path
from peliculas.views import crear_peliculas, listar_peliculas, crear_directores, listar_directores,crear_generos, listar_generos

urlpatterns = [
    path("crear-peliculas/", crear_peliculas ),
    path("listar-peliculas/", listar_peliculas),
    path("crear-directores/", crear_directores),
    path("listar-directores/", listar_directores),
    path("crear-generos/", crear_generos),
    path("listar-generos/", listar_generos),
]
