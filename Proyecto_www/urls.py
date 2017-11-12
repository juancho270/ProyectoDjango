from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_page, name='login'),
    url(r'^logout$', views.logout_page, name='logout'),
    url(r'^adm/registro$', views.registrarUsuario, name='registro_user'),
    url(r'^adm/consultar$', views.consultarUsuario, name='consulta_user'),
    url(r'^adm/seleccionar$', views.seleccionarUsuario, name='seleccionar_user'),
    url(r'^adm/modificar/(?P<nombre>\S+)$', views.modificarUsuario, name='modificar_user'),
    url(r'^ope/registro$', views.registrarEvento, name='registrar_evento'),
    url(r'^ope/consultar$', views.consultarEvento, name='consulta_Evento'),
    url(r'^adm/registrarNoticia$', views.registrarNoticia, name='registrar_noticia'),
    url(r'^adm/consultarNoticia$', views.consultarNoticia, name='consultar_noticia'),

]
