from django.db import models

class Musico(models.Model):
   nombre = models.CharField(max_length=50)
   apellido = models.CharField(max_length=50)
   instrumento = models.CharField(max_length=100) 

class Album(models.Model):
   musico = models.ForeignKey(Musico,on_delete=models.CASCADE)
   nombre = models.CharField(max_length=50)
   fechadeestreno = models.DateField()
   rating = models.IntegerField()


class Carnet(models.Model):
   identificador = models.CharField(max_length=10)
   fechaemision = models.DateField()

class Estudiante(models.Model):
   nombre = models.CharField(max_length=100)
   carnet = models.OneToOneField(Carnet,on_delete=models.CASCADE)


class Cursos(models.Model):
   nombre = models.CharField(max_length=100)
   duracion = models.TimeField()
   descripcion = models.TextField()
   estudiantes = models.ManyToManyField(Estudiante)