from django.db import models

# Create your models here.
class Empleado(models.Model):
    TIPO_IDENTIFICACION_CHOICES = (
        ('nit', 'NIT'),
        ('cc', 'Cédula de ciudadanía'),
    )
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    tipo_identificacion = models.CharField(max_length=3, choices=TIPO_IDENTIFICACION_CHOICES)
    identificacion = models.CharField(max_length=20)
    fechaingreso = models.DateField()
    salarioMensual = models.DecimalField(max_digits=10, decimal_places=2)
    cargo = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    
    
class Telefono(models.Model):
    TIPO_CHOICES = (
        ('cell', 'Celular'),
        ('tel', 'Teléfono'),
    )
    tipo = models.CharField(max_length=4, choices=TIPO_CHOICES)
    numero = models.CharField(max_length=20)
    indicativo = models.CharField(max_length=5)
    empleado = models.ForeignKey(Empleado, related_name='telefonos', on_delete=models.CASCADE)

class Email(models.Model):
    email = models.EmailField()
    empleado = models.ForeignKey(Empleado, related_name='emails', on_delete=models.CASCADE)