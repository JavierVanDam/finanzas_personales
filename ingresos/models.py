from django.core import validators
from django.db import models
from cuentas.models import Cuenta
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from cuentas.models import Cuenta

class CategoriaIngreso(models.Model):
    nombre = models.CharField(max_length=64, unique=True, 
                validators=[MinLengthValidator(limit_value=3, message="CATEG INGRESO, MIN 3 CARACTERES")])
    def __str__(self):
        return self.nombre


class Ingreso(models.Model):
    fecha = models.DateField()
    monto = models.FloatField(validators=[
            MinValueValidator(limit_value=100, message="monto inferior a 100"),
            MaxValueValidator(limit_value=100000, message="monto superior a %(limit_value)")])
    categoria = models.ForeignKey(CategoriaIngreso, related_name="tipo_de_ingreso", on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, related_name="usuario_carga_ingreso", on_delete=models.CASCADE)
    cuenta = models.ForeignKey(Cuenta, related_name="cuenta_ingreso", on_delete=models.CASCADE)
    fecha_carga = models.DateTimeField(auto_now_add=True)