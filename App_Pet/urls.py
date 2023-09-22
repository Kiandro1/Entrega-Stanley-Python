from django.urls import path
from django.contrib.auth.views import LogoutView
from App_Pet.views import *

urlpatterns = [
    path('',inicio, name="Inicio"),
    
    path('cliente/', cliente, name='Cliente'),
    path('lista-cliente/', lista_cliente, name= 'ListaCliente'),
    path('cliente-formulario/', cliente_formulario, name="ClienteFormulario"),
    path('buscar-cliente/', buscar_cliente, name="BuscarCliente"),
    path('resultado-cliente/',resultado_cliente, name='ResultadoCliente'),
    path('crea-cliente/', crea_cliente, name="CreaCliente"),
    path('elimina-cliente/<int:id>/', elimina_cliente, name="EliminaCliente"),
    path('editar-cliente/<int:id>', editar_cliente, name="EditarCliente"),
    
    path('mascota/', mascota, name="Mascota"),
    path('detalle-mascota/<pk>', MascotaDetail.as_view(), name="DetalleMascota"),
    path('mascota-delete/<pk>', MascotaDelete.as_view(), name="EliminaMascota"),
    path('lista-mascota/', MascotaList.as_view(), name="ListaMascota"),
    path('actualiza-mascota/<pk>', MascotaUpdate.as_view(), name="ActualizarMascota"),
    path('crea-mascota/', MascotaCreate.as_view(), name="CreaMascota"),
    
    path('alimento/', alimento, name='Alimento'),
    path('lista-alimento/', lista_alimento, name= 'ListaAlimento'),
    path('alimento-formulario/', alimento_formulario, name="AlimentoFormulario"),
    path('buscar-alimento/', buscar_alimento, name= 'BuscarAlimento'),
    path('resultado-alimento/',resultado_alimento, name= 'ResultadoAlimento'),
    path('crea-alimento/', crea_alimento, name="CreaAlimento"),
    path('elimina-alimento/<int:id>', elimina_alimento, name="EliminaAlimento"),
    path('editar-alimento/<int:id>', editar_alimento, name= 'EditarAlimento'),
    
    path('login/', loginView, name="Login"),
    path('registrar/', register, name="Registrar"),
    path('logout/', LogoutView.as_view(template_name="inicio.html"), name="Logout"),
    path('editar-perfil/', editar_perfil, name="EditarPerfil"),
    path('agregar-avatar/', agregar_avatar, name="AgregarAvatar"),
]