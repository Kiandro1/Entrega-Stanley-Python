from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Mascota, Cliente, Alimento_Pet, Avatar
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .forms import ClienteFormulario, MascotaFormulario, AlimentoFormulario
# Create your views here.
def mascota(req, nombre, nombre_cliente):

    nombre_pet = Mascota(nombre=nombre, nombre_cliente=nombre_cliente)
    nombre_pet.save()

    return HttpResponse(f"""
        <p>Nombre de mascota: {nombre_pet.nombre} - Nombre de cliente: {nombre_pet.nombre_cliente} agregado!</p>
    """)
# def cliente(req, nombre, movil):

#     cliente_mascota = Cliente(nombre=nombre, movil=movil)
#     cliente.save()

#     return HttpResponse(f"<p>Cliente: {cliente_mascota.nombre} - Móvil: {cliente_mascota.movil} agregado!</p>")
    


def inicio(req):
        
        return render(req, "inicio.html")

def lista_mascota(req):
    
    lista = Mascota.objects.all()

    return render(req, "lista_mascota.html", {"lista_mascota": lista})



def alimento(req):

    return render(req, "alimento.html")

def lista_alimento(req):  
    
    lista = Alimento_Pet.objects.all()

    return render(req, "lista_alimento.html", {"lista_mascota": lista})

@login_required
def lista_cliente(req):

    lista = Cliente.objects.all()

    return render(req, "lista_ciente.html", {"lista_cliente": lista})

def cliente_formulario(req):

    print('method', req.method)
    print('post', req.POST)

    if req.method == 'POST':

        miFormulario = ClienteFormulario(req.POST)
        
        if miFormulario.is_valid():

            print(miFormulario.cleaned_data)
            data = miFormulario.cleaned_data

            nombre_cliente = Cliente(nombre=data["nombre"], apellido=data["apellido"], movil=data['movil'], email=data['email'])
            nombre_cliente.save()
            return render(req, "inicio.html", {"mensaje": "Cliente creado con éxito"})
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})
    else:

        miFormulario = ClienteFormulario()

        return render(req, "cliente_formulario.html", {"miFomulario": miFormulario})

def busqueda_cliente(req):

    return render(req, "busqueda_cliente.html")

def buscar_cliente(req):

    if req.GET["nombre"]:
        nombre = req.GET["nombre"]
        movil = Cliente.objects.filter(nombre__icontains=nombre)
        if movil:
            return render(req, "resultado_busqueda.html", {"movil": movil})
    else:
        return HttpResponse('No escribiste ninguna nombre')

@staff_member_required(login_url='/App_Pet/login')
def lista_cliente(req):

    clientes = Cliente.objects.all()

    return render(req, "leer_cliente.html", {"clientes": clientes})

def crea_cliente(req):

    if req.method == 'POST':

        miFormulario = ClienteFormulario(req.POST)
        
        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            cliente = Cliente(nombre=data["nombre"], apellido=data["apellido"], movil=data["movil"], email=data["email"])
            cliente.save()
            return render(req, "inicio.html", {"mensaje": "Cliente creado con éxito"})
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})
    else:

        miFormulario = ClienteFormulario()

        return render(req, "profesor_formulario.html", {"miFomulario": miFormulario})


def editar_cliente(req, id):

    clientes = Cliente.objects.get(id=id)

    if req.method == 'POST':

        miFormulario = ClienteFormulario(req.POST)
        
        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            clientes.nombre = data["nombre"]
            clientes.apellido = data["apellido"]
            clientes.email = data["movil"]
            clientes.profesion = data["email"]
            clientes.save()
            return render(req, "inicio.html", {"mensaje": "Cliente actualizado con éxito"})
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})
    else:

        miFormulario = ClienteFormulario(initial={
            "nombre": clientes.nombre,
            "apellido": clientes.apellido,
            "movil": clientes.movil,
            "email": clientes.email,
        })

        return render(req, "editar_cliente.html", {"miFomulario": miFormulario, "id": clientes.id})
    

# class ClienteList(ListView):
#     model = Cliente
#     template_name = "cliente_list.html"
#     context_object_name = "cliente"


# class ClienteDetail(LoginRequiredMixin, DetailView):
#     model = Cliente
#     template_name = "cliente_detail.html"
#     context_object_name = "cliente"

# class ClienteCreate(CreateView):
#     model = Cliente
#     template_name = "cliente_create.html"
#     fields = ["nombre", "apellido", "movil", "email"]
#     success_url = "/app-pet/"

# class ClienteUpdate(UpdateView):
#     model = Cliente
#     template_name = "cliente_update.html"
#     fields = ("__all__")
#     success_url = "/App_Pet/"


def loginView(req):

    if req.method == 'POST':

        miFormulario = AuthenticationForm(req, data=req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            usuario = data["username"]
            psw = data["password"]

            user = authenticate(username=usuario, password=psw)

            if user:
                login(req, user)
                return render(req, "inicio.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(req, "inicio.html", {"mensaje": "Datos incorrectos"})

        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})

    else:
        miFormulario = AuthenticationForm()
        return render(req, "login.html", {"miFomulario": miFormulario})

def register(req):

    if req.method == 'POST':

        miFormulario = UserCreationForm(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            usuario = data["username"]

            miFormulario.save()

            return render(req, "inicio.html", {"mensaje": f"Usuario {usuario} creado con éxito!"})

        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})

    else:
        miFormulario = UserCreationForm()
        return render(req, "registro.html", {"miFomulario": miFormulario})

def mascota_formulario(req):

    print('method', req.method)
    print('post', req.POST)

    if req.method == 'POST':

        miFormulario = MascotaFormulario(req.POST)
        
        if miFormulario.is_valid():

            print(miFormulario.cleaned_data)
            data = miFormulario.cleaned_data

            nombre_mascota = Mascota(nombre=data["nombre"], nombre_cliente=data["nombre_cliente"], raza=data['raza'], peso=data['peso'])
            nombre_mascota.save()
            return render(req, "inicio.html", {"mensaje": "Mascota creado con éxito"})
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})
    else:

        miFormulario = MascotaFormulario()

        return render(req, "mascota_formulario.html", {"miFomulario": miFormulario})

def busqueda_mascota(req):

    return render(req, "busqueda_mascota.html")

def buscar_mascota(req):

    if req.GET["nombre"]:
        nombre = req.GET["nombre"]
        nombre_cliente = Mascota.objects.filter(nombre__icontains=nombre)
        if nombre_cliente:
            return render(req, "resultado_mascota.html", {"nombre_cliente": nombre_cliente})
    else:
        return HttpResponse('No escribiste ninguna nombre')
    
    
def mascota_alimento(req):

    print('method', req.method)
    print('post', req.POST)

    if req.method == 'POST':

        miFormulario = Alimento_Pet(req.POST)
        
        if miFormulario.is_valid():

            print(miFormulario.cleaned_data)
            data = miFormulario.cleaned_data

            marca_alimento = AlimentoFormulario(marca=data["marca_alimento"], raza_pet=data["raza"])
            marca_alimento.save()
            return render(req, "inicio.html", {"mensaje": "Marca creada"})
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})
    else:

        miFormulario = AlimentoFormulario()

        return render(req, "alimento_formulario.html", {"miFomulario": miFormulario})

def busqueda_alimento(req):

    return render(req, "busqueda_alimento.html")

def buscar_alimento(req):

    if req.GET["marca"]:
        marca = req.GET["marca"]
        raza_especie = Alimento_Pet.objects.filter(marca__icontains=marca)
        if raza_especie:
            return render(req, "resultado_alimento.html", {"raza_especie": raza_especie})
    else:
        return HttpResponse('No escribiste ninguna nombre')


# Create your views here.
