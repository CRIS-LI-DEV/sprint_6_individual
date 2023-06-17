
from django.db import models
from django.contrib.auth.models import User 



class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20)
    profesor_jefe = models.ForeignKey('Profesor', on_delete=models.CASCADE,null=True)
  
    def __str__(self):
        return self.nombre


class Profesor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
   
    
    def __str__(self):
        return self.nombre
    class Meta:
         permissions = [
        ("permiso_profesor", "Puede acceder a las interfaces de profesor")
        ]

class Alumno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)

    curso = models.ForeignKey('Curso', on_delete=models.CASCADE,null=True)
  
    
    def __str__(self):
        
        return self.nombre

    class Meta:
         permissions = [
        ("permiso_alumno", "Puede acceder a las interfaces de alumno")
        ]


class Inspector(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
  
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    def __str__(self):
        
        return self.nombre

    class Meta:
         permissions = [
        ("permiso_inspector", "Puede acceder a las interfaces de inspector")
        ]