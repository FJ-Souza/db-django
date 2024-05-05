from django.urls import path
from siteStudioJr.views import *
urlpatterns = [
    path("", index, name = "index"),
    path("pagina/", pagina, name = "pagina"),
    path("agendar/", agendar_secao, name = "agendar_secao"),
    path("listar/", listar_clientes, name = "listar_clientes")
]