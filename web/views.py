from django.shortcuts import render, HttpResponseRedirect
from .forms import UsuarioForm, UserUpdateForm,CrearInmuebleForm
from .models import *

# Create your views here.

def indexView(request):
    return render(request,'index.html')

def usuario_new(request):
    form = UsuarioForm()
    return render(request,'user_new.html',{ 'form' : form})

def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        if u_form.is_valid():
            u_form.save()
            return HttpResponseRedirect('/')
    else:
        u_form = UserUpdateForm(instance=request.user)
        context={'u_form': u_form}
        return render(request,'update_profile.html', context)
    
def inmueble_new(request):
    if request.method == 'POST':
        i_form = CrearInmuebleForm(request.POST,instance=request.user)
        if i_form.is_valid():
            i_form.save()
            return HttpResponseRedirect('/')
    
    else:
        i_form = CrearInmuebleForm(instance=request.user)
        return render(request,'inmueble_new.html',{'i_form': i_form})
    
def enlistar(request):
    inmuebles = Inmueble.objects.all()
    return render(request,'enlistar.html',{'inmuebles': inmuebles})
    
