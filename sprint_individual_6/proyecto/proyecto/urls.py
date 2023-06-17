
from django.contrib import admin
from django.urls import path
from aplicacion.views import (registro,
login_usuario,
perfil_alumno,perfil_profesor,perfil_inspector,
logout_view,home,logueo_existoso
)
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/',registro,name="registro"),
    
    path('login_view/',login_usuario,name="login"),
   
    path('logueo_exisitoso/',logueo_existoso,name='logueo_existoso'),
    path('perfil_inspector/',login_required(perfil_inspector),name="p_inspector"),
    path('perfil_alumno/',login_required(perfil_alumno) ,name="p_alumno"),
    path('perfil_profesor/',login_required(perfil_profesor),name="p_profesor"),
    path('logout_view/',logout_view,name="logout"),
    path('home/',home,name="home"),
    path('',home,name="home"),
]
