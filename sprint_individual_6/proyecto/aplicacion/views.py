from django.shortcuts import render, redirect
from aplicacion.models import (Alumno,Inspector,Profesor)
from aplicacion.forms import (Registro,LoginForm)
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password 
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import permission_required,login_required

def registro(request):
    if request.method == 'POST':

        formulario = Registro(request.POST)

        if formulario.is_valid():
            nombre_usuario = formulario.cleaned_data['nombre_usuario']
            nombre = formulario.cleaned_data['nombre']
            apellido = formulario.cleaned_data['apellido']
            email = formulario.cleaned_data['email']
            clave = formulario.cleaned_data['clave']
            direccion = formulario.cleaned_data['direccion']
            ciudad = formulario.cleaned_data['ciudad']
            grupo = formulario.cleaned_data['grupo']
            usuario = User(
                 username=nombre_usuario,
                 first_name=nombre,
                 last_name=apellido,
                 email=email)
            usuario.password = make_password(clave)
            usuario.save()
            print(grupo)
            if  grupo == 'inspector':
                print("LEgue")
                perfil = Inspector(
                user=usuario,
                direccion=direccion,
                ciudad=ciudad
                )
                perfil.save()
                grupo = Group.objects.get(name='inspectores')  
                usuario.groups.add(grupo)
            
            if  grupo == 'profesor':
                perfil = Profesor(
                user=usuario,
                direccion=direccion,
                ciudad=ciudad
                ) 
                perfil.save()
                grupo = Group.objects.get(name='profesores')
                usuario.groups.add(grupo)
            
            if  grupo == 'alumno':
                perfil = Alumno(
                user=usuario,
                direccion=direccion,
                ciudad=ciudad
                )
                perfil.save()
                grupo = Group.objects.get(name='alumnos') 
                usuario.groups.add(grupo) 
            
        return redirect('/logueo_exisitoso/')

    else:
        formulario = Registro()
        return render(request, 'registro.html', context={'formulario': formulario})



def login_usuario(request):
    if request.method == 'POST':

        formulario = LoginForm(request.POST)

        print(formulario['clave'].value())

        if formulario.is_valid():
            username = formulario.cleaned_data['usuario']
            password = formulario.cleaned_data['clave']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            print(user)
            print(f"USER ID :{user.id}")
            
            profesor = Profesor.objects.filter(
                    user_id=user.id).count()
            inspector = Inspector.objects.filter(
                    user_id=user.id).count()
            alumno = Alumno.objects.filter(
                    user_id=user.id).count()

            if profesor==1 and inspector == 0 and alumno == 0:
                    return redirect('/perfil_profesor/')
            if profesor == 0 and inspector == 1 and alumno == 0:
                    return redirect('/perfil_inspector/')
            if profesor == 0 and inspector == 0 and alumno == 1:
                    return redirect('/perfil_alumno/')    
           
                
    else:
        formulario = LoginForm()
        return render(request, 'login.html', {'formulario': formulario})

@permission_required('aplicacion.permiso_alumno')

def perfil_alumno(request):
    context = {}
    return render(request, 'perfil_alumno.html', context)    

@permission_required('aplicacion.permiso_profesor')
def perfil_profesor(request):
    context = {}
    return render(request, 'perfil_profesor.html', context)    

@permission_required('aplicacion.permiso_inspector')
def perfil_inspector(request):
    context = {



    }
    return render(request, 'perfil_inspector.html', context) 

def logout_view(request):
    print(request.user)
    print('logout')
    logout(request)
    return redirect('/')   

def home(request):
    context = {}
    return render(request, 'home.html', context) 
    

def logueo_existoso(request):
    return render (request,'logueate.html')