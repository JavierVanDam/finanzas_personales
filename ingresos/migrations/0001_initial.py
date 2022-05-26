# Generated by Django 3.1 on 2022-05-02 20:44

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cuentas', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaIngreso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64, unique=True, validators=[django.core.validators.MinLengthValidator(limit_value=3, message='CATEG INGRESO, MIN 3 CARACTERES')])),
            ],
        ),
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('monto', models.FloatField(validators=[django.core.validators.MinValueValidator(limit_value=100, message='monto inferior a 100'), django.core.validators.MaxValueValidator(limit_value=100000, message='monto superior a %(limit_value)')])),
                ('fecha_carga', models.DateTimeField(auto_now_add=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tipo_de_ingreso', to='ingresos.categoriaingreso')),
                ('cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cuenta_ingreso', to='cuentas.cuenta')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_carga_ingreso', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]