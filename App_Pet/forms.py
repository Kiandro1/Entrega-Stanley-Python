from django import forms

class ClienteFormulario(forms.Form):

    nombre = forms.CharField(required=True)
    apellido = forms.CharField(required=True)
    movil = forms.IntegerField(required=True)
    email = forms.EmailField(required=True)


class MascotaFormulario(forms.Form):

    nombre = forms.CharField(required=True)
    nombre_cliente = forms.CharField(required=True)
    raza = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    peso = forms.FloatField()
    
class AlimentoFormulario(forms.Form):

    marca = forms.CharField(required=True)
    raza_pet = forms.CharField(required=True)
