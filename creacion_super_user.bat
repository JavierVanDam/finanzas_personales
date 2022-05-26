echo "from django.contrib.auth.models import User; us_creado = User.objects.create_superuser('javier', 'javiervandam@gmail.com', 'pass');print(us_creado)" > python manage.py shell


pause

@REM si lo haces directo en la shell
@REM from django.contrib.auth.models import User
@REM us_creado = User.objects.create_superuser('javier', 'javiervandam@gmail.com', 'pass')
@REM print(us_creado)