# Generated by Django 3.1 on 2022-05-12 13:25

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cuentas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaGasto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Gasto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=None)),
                ('monto', models.FloatField(default=0, error_messages={'required': 'ERROR MONTO'}, validators=[django.core.validators.MinValueValidator(1000, 'NO PUEDE SER INFERIOR A %(limit_value)s Y VOS PUSISTE %(show_value)s')])),
                ('cuotas', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(24)])),
                ('comprobante', models.ImageField(default='comprobantes_gastos/imagen_default_gastos.jpg', null=True, upload_to='comprobantes_gastos/')),
                ('categoria', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='categoria_tarasca', to='gastos.categoriagasto')),
                ('forma_pago', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='forma_de_pago', to='cuentas.cuenta')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_gasto', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
