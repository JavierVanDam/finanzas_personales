from django.db import models
from django.core.exceptions import ValidationError

TIPOS_CUENTA = (('INGRESOS', 'INGRESOS'), ('GASTOS', 'GASTOS'), ('AMBOS', 'AMBOS'))


class Cuenta(models.Model):
    nombre = models.CharField(max_length=64)
    tipo_cuenta = models.CharField(max_length=64, choices=TIPOS_CUENTA)
    permite_cuotas = models.BooleanField(default=False)

    def clean(self):
        #el serializer no le da bola a esto
        if self.tipo_cuenta == 'INGRESOS' and self.permite_cuotas==True:
            raise ValidationError("LAS CUENTAS DE INGRESO NO PERMITEN CUOTAS")

    def __str__(self):
        return self.nombre
