from django.db import models

class Student(models.Model):
    identificacion = models.IntegerField() 
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    cursos = models.CharField(max_length=255)
    edad = models.IntegerField()
    telefono = models.IntegerField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Profesor(models.Model):
    identificacion = models.IntegerField() 
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    cursos = models.CharField(max_length=255)
    edad = models.IntegerField()
    telefono = models.IntegerField()
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    

class Curso(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    duracion_meses = models.IntegerField()
    imagen = models.ImageField(upload_to='cursos/', null=True, blank=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre
    
    
    