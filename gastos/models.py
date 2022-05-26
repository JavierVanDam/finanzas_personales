from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from cuentas.models import Cuenta
from django.contrib.auth.models import User


class CategoriaGasto(models.Model):
    nombre = models.CharField(max_length=64)
    def __str__(self):
        return self.nombre



class Gasto(models.Model):
    fecha = models.DateField(default=None)
    monto = models.FloatField(
        default=0, error_messages={'required': 'ERROR MONTO'},
        validators=[MinValueValidator(1000, "NO PUEDE SER INFERIOR A %(limit_value)s Y VOS PUSISTE %(show_value)s")])
    cuotas = models.IntegerField( default=1 , validators=[MinValueValidator(1), MaxValueValidator(24)])
    categoria = models.ForeignKey(CategoriaGasto, related_name='categoria_tarasca', on_delete=models.CASCADE, default=0)  # si no le pongo default, aparece ------
    forma_pago = models.ForeignKey(Cuenta, related_name='forma_de_pago', on_delete=models.CASCADE, default=0)
    comprobante = models.ImageField(upload_to='comprobantes_gastos/', default='comprobantes_gastos/imagen_default_gastos.jpg', null=True)
    usuario = models.ForeignKey(User, related_name='usuario_gasto', on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.fecha, self.monto)
