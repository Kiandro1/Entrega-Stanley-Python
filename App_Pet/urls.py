from django.urls import path
from django.contrib.auth.views import LogoutView
from App_Pet.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('agrega-cliente/<nombre>/<movil>', crea_cliente),
    path('lista-cliente/', lista_cliente),
    path('cliente-formulario/', cliente_formulario, name="ClienteFormulario"),
    path('busqueda-cliente/', busqueda_cliente, name="BusquedaCliente"),
    path('resultado-cliente/', buscar_cliente, name="BuscarCliente"),
    path('lista-cliente/', lista_cliente, name="ListaCliente"),
    path('crea-ciente/', crea_cliente, name="CreaCliente"),
    path('editar-cliente/', editar_cliente, name="EditarCliente"),
    path('mascota/', mascota, name="Mascota"),
    path('lista-mascota/', lista_mascota, name="ListaMascota"),
    path('mascota-formulario/<int:id>', mascota_formulario, name="MascotaFormulario"),
    path('busqueda-mascota/<int:id>', busqueda_mascota, name="BusquedaMascota"),
    path('resultado-mascota/', buscar_mascota, name="BuscarCliente"),
    path('alimento/', alimento, name='Alimento'),
    path('mascota-alimento/', mascota_alimento, name="MascotaAlimento"),
    path('buscar-alimento/', buscar_alimento, name="BuscarAlimento"),
    path('busqueda-alimento/', busqueda_alimento, name="BusquedaAlimento"),
    # path('lista-cliente/', ClienteList.as_view(), name="ListaClientes"),
    # path('detalle-curso/<pk>', ClienteDetail.as_view(), name="DetalleClientes"),
    # path('crea-curso/', ClienteCreate.as_view(), name="CreaCursos"),
    # path('actualiza-curso/<pk>', ClienteUpdate.as_view(), name="ActualizarClientes"),
    # path('login/', loginView, name="Login"),
    # path('registrar/', register, name="Registrar"),
    path('logout/', LogoutView.as_view(template_name="inicio.html"), name="Logout"),
]