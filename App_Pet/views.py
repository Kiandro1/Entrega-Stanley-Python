from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest
from .models import Mascota, Cliente, Alimento_Pet, Avatar
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .forms import ClienteFormulario, AlimentoFormulario, UserEditForm, AvatarFormulario
# Create your views here.
def inicio(request):
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        return render(request, "inicio.html", {"url": avatar.imagen.url})
    except:
        return render(request, "inicio.html")

def cliente(request):

    return render(request, 'cliente.html')

def cliente_formulario(request):

    print('method', request.method)
    print('post', request.POST)

    if request.method == 'POST':

        miFormulario = ClienteFormulario(request.POST)

        if miFormulario.is_valid():

            print(miFormulario.cleaned_data)
            data = miFormulario.cleaned_data

            nombre_cliente = Cliente(nombre=data["nombre"], apellido=data["apellido"], movil=data['movil'], email=data['email'])
            nombre_cliente.save()
            return render(request, "inicio.html", {"mensaje": "Cliente creado con éxito"})
        else:
            return render(request, "inicio.html", {"mensaje": "Formulario inválido"})
    else:

        miFormulario = ClienteFormulario()

        return render(request, "cliente_formulario.html", {"miFomulario": miFormulario})

def buscar_cliente(request):

    if request.GET.get("nombre"):
        nombre = request.GET.get("nombre", "defoult")
        movil = Cliente.objects.filter(nombre__icontains=nombre)
        if movil:
            return render(request, "busqueda_cliente.html", {"movil": movil})
    else:
        return render(request, "busqueda_cliente.html",{'mensaje':'No escribiste ningun nombre'})
    
def resultado_cliente(request):
    return render(request, 'cliente_resultado.html')

@staff_member_required(login_url='/App_Pet/login')
def lista_cliente(request):

    clientes = Cliente.objects.all()

    return render(request, "lista_cliente.html", {"clientes": clientes})

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

        return render(req, "cliente_formulario.html", {"miFomulario": miFormulario})


def editar_cliente(request,id):

    clientes = Cliente.objects.get(id=id)

    if request.method == 'POST':

        miFormulario = ClienteFormulario(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            clientes.nombre = data["nombre"]
            clientes.apellido = data["apellido"]
            clientes.movil = data["movil"]
            clientes.email = data["email"]
            clientes.save()
            return render(request, "inicio.html", {"mensaje": "Cliente actualizado con éxito"})

        else:

            return render(request, "inicio.html", {"mensaje": "Formulario inválido"})
    else:

        miFormulario = ClienteFormulario(initial={
            "nombre": clientes.nombre,
            "apellido": clientes.apellido,
            "movil": clientes.movil,
            "email": clientes.email,
        })

        return render(request, "editar_cliente.html", {"miFomulario": miFormulario, "id": clientes.id})

def elimina_cliente(request,id):
    
    if request.method == 'POST':
        clientes = Cliente.objects.get(id=id)
        clientes.delete()
        
        cliente = Cliente.objects.all()

        return render(request, 'elimina_cliente.html', {'id':cliente,'mensaje': 'Cliente eliminado'})
    else:
        return render (request, 'lista_cliente.html', {'mensaje':'Cliente no eliminado'})

@login_required
def mascota(request):
    return render(request,'mascota.html')

class MascotaList(ListView):
    model = Mascota
    template_name = "mascota_list.html"
    context_object_name = "mascotas"

class MascotaDetail(LoginRequiredMixin, DetailView):
    model = Mascota
    template_name = "mascota_detalle.html"
    context_object_name = "mascotas"

class MascotaCreate(CreateView):
    model = Mascota
    template_name = "mascota_create.html"
    fields = ["nombre", "nombre_cliente", "raza", "peso","edad"]
    success_url = "/Inicio/"

class MascotaUpdate(UpdateView):
    model = Mascota
    template_name = "mascota_actualiza.html"
    fields = ("__all__")
    success_url = "/app_pet/"

class MascotaDelete(DeleteView):
    model = Mascota
    template_name = "mascota_delete.html"
    success_url = "/app-pet/"


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

def editar_perfil(req):

    usuario = req.user

    if req.method == 'POST':

        miFormulario = UserEditForm(req.POST, instance=req.user)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.set_password(data["password1"])
            usuario.save()
            return render(req, "inicio.html", {"mensaje": "Perfil actualizado con éxito"})
        else:
            return render(req, "edita_perfil.html", {"miFomulario": miFormulario})
    else:

        miFormulario = UserEditForm(instance=req.user)

        return render(req, "edita_perfil.html", {"miFomulario": miFormulario})

def agregar_avatar(req):

    if req.method == 'POST':

        miFormulario = AvatarFormulario(req.POST, req.FILES)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            avatar = Avatar(user=req.user, imagen=data["imagen"])

            avatar.save()

            return render(req, "inicio.html", {"mensaje": f"Avatar actualizado con éxito!"})

        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})

    else:
        miFormulario = AvatarFormulario()
        return render(req, "agregarAvatar.html", {"miFomulario": miFormulario})



def alimento(req):
    return render(req, "alimento.html")

def alimento_formulario(req):
    
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

def buscar_alimento(request):

    if request.GET.get('marca'):
        marca = request.GET.get('marca','defoult')
        raza_especie = Alimento_Pet.objects.filter(marca__icontains=marca)
        if raza_especie:
            return render(request, "resultado_alimento.html", {"raza_especie": raza_especie})
    else:
        return render(request,"busqueda_alimento.html",{'mensaje':'No escribiste ninguna nombre'})

def resultado_alimento(request):
    return render(request, "resultado_alimento.html")

@staff_member_required(login_url='/App_Pet/login')
def lista_alimento(request):

    alimentos = Alimento_Pet.objects.all()

    return render(request, "lista_alimento.html", {"alimentos": alimentos})

def crea_alimento(req):

    if req.method == 'POST':

        miFormulario = AlimentoFormulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            alimento = AlimentoFormulario(marca=data["marca"], raza=data["raza"])
            alimento.save()
            return render(req, "inicio.html", {"mensaje": "Alimento creado con éxito"})
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})
    else:

        miFormulario = AlimentoFormulario()

        return render(req, "alimento_formulario.html", {"miFomulario": miFormulario})
def editar_alimento(request,id):

    alimentos = Alimento_Pet.objects.get(id=id)

    if request.method == 'POST':

        miFormulario = AlimentoFormulario(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            alimentos.marca = data["marca"]
            alimentos.raza_pet = data["raza_pet"]
            alimentos.save()
            return render(request, "inicio.html", {"mensaje": "Alimento actualizado con éxito"})

        else:

            return render(request, "inicio.html", {"mensaje": "Formulario inválido"})
    else:

        miFormulario = AlimentoFormulario(initial={
            "marca": alimentos.marca,
            "raza": alimentos.raza_pet,
        })

        return render(request, "editar_alimento.html", {"miFomulario": miFormulario, "id": alimentos.id})
def elimina_alimento(request,id):
    
    if request.method == 'POST':
        alimento = Alimento_Pet.objects.get(id=id)
        alimento.delete()
        
        alimentos = Alimento_Pet.objects.all()

        return render(request, 'elimina_alimento.html', {'id':alimentos,'mensaje': 'Alimento eliminado'})
    else:
        return render (request, 'lista_alimento.html', {'mensaje':'Alimento no eliminado'})
# Create your views here.
