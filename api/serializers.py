from distutils.command.upload import upload
from django.contrib.auth.models import User
from rest_framework import serializers

from cuentas.models import Cuenta
from ingresos.models import Ingreso, CategoriaIngreso
from gastos.models import Gasto, CategoriaGasto


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'id')


class CuentaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cuenta
        fields = ['id', 'nombre', 'tipo_cuenta', 'permite_cuotas']

    def validate(self, data):
        if data['tipo_cuenta'] == "INGRESOS" and data['permite_cuotas'] == True:
            raise serializers.ValidationError(
                "LAS CUENTAS DE INGRESO NO PERMITEN CUOTAS")
        return data


class CategoriaIngresoSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoriaIngreso
        fields = '__all__'


class IngresoSerializer(serializers.ModelSerializer):
    '''el q uso para los gets, donde solo mando el id de usuario y de categoria'''
    #categoria = serializers.StringRelatedField() #devuelve lo definido en def __str__(self):
    categoria = CategoriaIngresoSerializer()
    usuario = UsuarioSerializer()
    cuenta = CuentaSerializer()
    fecha_carga = serializers.DateTimeField(format="%Y-%m-%d")

    class Meta:
        model = Ingreso
        fields = '__all__'



class IngresoSerializerSimplificado(serializers.ModelSerializer):
    '''el q uso para los posts, donde solo mando el id de usuario y de categoria'''
    
    class Meta:
        model = Ingreso
        fields = '__all__'


class CategoriaGastoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaGasto
        fields = '__all__'



class GastoSerializer(serializers.ModelSerializer):
    '''el q uso p los gets'''
    usuario = UsuarioSerializer()
    forma_pago = CuentaSerializer()
    categoria = CategoriaGastoSerializer()
    
    class Meta:
        model = Gasto
        fields = '__all__'


class GastoSerializerPosts(serializers.ModelSerializer):
    '''el q uso p los posts'''
    class Meta:
        model = Gasto
        fields = '__all__'


class FileSerializer(serializers.Serializer):
    file = serializers.FileField()
    class Meta:
        fields = ['file']
