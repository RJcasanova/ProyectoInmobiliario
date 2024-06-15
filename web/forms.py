from django import forms
from .models import Usuario, Inmueble
from django.contrib.auth.models import User

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ('nombres','apellidos','rut','direccion','telefono','correo')

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields =['first_name','last_name','email']

class CrearInmuebleForm(forms.ModelForm):

    class Meta:
        model = Inmueble
        fields = ('nombre','descripcion','m2_construidos','m2_totales','cantidad_estacionamientos','cantidad_habitaciones','cantidad_banos',
                  'direccion','comuna','tipo_inmueble','precio_arriendo')
        
class InmuebleUpdateForm(forms.ModelForm):

    class Meta:
        model = Inmueble
        fields = ('nombre','descripcion','m2_construidos','m2_totales','cantidad_estacionamientos','cantidad_habitaciones','cantidad_banos',
                  'direccion','comuna','tipo_inmueble','precio_arriendo')