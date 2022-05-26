from datetime import datetime
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.sessions.models import Session

from rest_framework import generics, exceptions
from rest_framework.parsers import JSONParser, FileUploadParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView

from cuentas.models import Cuenta
from ingresos.models import Ingreso, CategoriaIngreso
from .serializers import *

# CBVs


class GastoListCreate(generics.ListCreateAPIView):
    queryset = Gasto.objects.all()
    permission_classes = [IsAuthenticated]

    # serializer_class = IngresoSerializer
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GastoSerializer
        elif self.request.method == 'POST':
            return GastoSerializerPosts
        else:
            raise exceptions.MethodNotAllowed(self.request.method)


class CategoriaGastoListCreate(generics.ListCreateAPIView):
    queryset = CategoriaGasto.objects.all()
    serializer_class = CategoriaGastoSerializer
    permission_classes = [IsAuthenticated]


class CuentasRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer
    permission_classes = [IsAuthenticated]


class CuentasListCreate(generics.ListCreateAPIView):
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer
    permission_classes = [IsAuthenticated]


class CuentasRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer
    permission_classes = [IsAuthenticated]


class CategoriaIngresoListCreate(generics.ListCreateAPIView):
    queryset = CategoriaIngreso.objects.all()
    serializer_class = CategoriaIngresoSerializer


class CategoriaIngresoRetrieveUpdateDestroy(
        generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoriaIngreso.objects.all()
    serializer_class = CategoriaIngresoSerializer


class IngresoListCreate(generics.ListCreateAPIView):
    queryset = Ingreso.objects.all()
    permission_classes = [IsAuthenticated]

    # serializer_class = IngresoSerializer
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return IngresoSerializer
        elif self.request.method == 'POST':
            return IngresoSerializerSimplificado
        else:
            raise exceptions.MethodNotAllowed(self.request.method)


class IngresoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingreso.objects.all()
    serializer_class = IngresoSerializer


class FileUploadView(APIView):
    parser_classes = (MultiPartParser, )

    def put(self, request, pk):
        gastoUpload = get_object_or_404(Gasto, pk=pk)
        print(gastoUpload)
        file_obj = request.data['file']
        print(file_obj.name)
        gastoUpload.comprobante = file_obj
        gastoUpload.save()

        return Response({'ok': 'no tan mal'}, status=204)


@api_view(['POST'])
@csrf_exempt
def login_view(request):
    if request.method == "POST":
        #ver: xq parsea request y devuelve responses con clases de django y no de drf?
        data = JSONParser().parse(request)
        print(data)
        user = authenticate(request,
                            username=data['username'],
                            password=data['password'])
        if user is None:  #error logueo
            return JsonResponse(
                {'error': 'no se encontro usuario y contraseña'}, status=400)

        else:  #logueo ok => puede o no tener token
            try:
                token = Token.objects.get(user=user)
            except:
                token = Token.objects.create(user=user)

            return JsonResponse({
                'token': str(token),
                'id': user.id
            },
                                status=201)
    else:
        return JsonResponse({'error': 'metodo no permitido'}, status=400)


@csrf_exempt
def logout_view(request):
    if request.method == "POST":
        #ver: xq parsea request y devuelve responses con clases de django y no de drf?
        data = JSONParser().parse(request)
        tokenUsuarioDesloguear = data['tokenazo']
        print(data)
        try:
            #dado el token, puedo sacar el usuario y las sesiones activas
            token = get_object_or_404(Token, key=tokenUsuarioDesloguear)
            usuario = token.user
            sesionesActivas = Session.objects.filter(
                expire_date__gte=datetime.now())
            if sesionesActivas.exists():
                for sesion in sesionesActivas:
                    dato_sesion = sesion.get_decoded()
                    if usuario.id == int(dato_sesion.get('_auth_user_id')):
                        sesion.delete()
            token.delete()

            return JsonResponse(
                {
                    'OK':
                    f'deslogueado usuario {usuario.id} con token {tokenUsuarioDesloguear}'
                },
                status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'error': str(e)},
                                status=status.HTTP_400_BAD_REQUEST)
