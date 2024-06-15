from django.db import models

# Create your models here.

class Region(models.Model):
    id = models.IntegerField(auto_created=True,primary_key=True)
    nombre = models.CharField(max_length=100,null=False)

class Comuna(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    id_region = models.ForeignKey(Region,on_delete=models.CASCADE)

class Tipo_usuario(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=15)

class Usuario(models.Model):
    nombres = models.CharField(max_length=50,null=False)
    apellidos = models.CharField(max_length=50,null=False)
    rut = models.CharField(max_length=9,primary_key=True)
    direccion = models.CharField(max_length=50,null=False)
    telefono = models.IntegerField(null=False)
    correo = models.EmailField(null=False)
    tipo_usuario = models.ForeignKey(Tipo_usuario,on_delete=models.CASCADE)

class Tipo_inmueble(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=15)

class Inmueble(models.Model):
    id = models.IntegerField(auto_created=True,primary_key=True)
    nombre = models.CharField(max_length=50,null=False)
    descripcion = models.TextField(null=False)
    m2_construidos = models.IntegerField(null=False)
    m2_totales = models.IntegerField(null=False)
    cantidad_estacionamientos = models.IntegerField(null=False)
    cantidad_habitaciones = models.IntegerField(null=False)
    cantidad_banos = models.IntegerField(null=False)
    direccion = models.CharField(max_length=50,null=False)
    comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE)
    tipo_inmueble = models.ForeignKey(Tipo_inmueble,on_delete=models.CASCADE)
    precio_arriendo = models.IntegerField(null=False)


