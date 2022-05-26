from django.urls import path, include
from .views import *

app_name = 'api'

urlpatterns = [
    path("cuentas/", CuentasListCreate.as_view(), name="cuentas-list-create"),
    path("cuentas/<int:pk>/", CuentasRetrieveUpdateDestroy.as_view(), name="cuentas-delete-update-detail"), 
    path("categ_ingresos/", CategoriaIngresoListCreate.as_view(), name="categ-ingresos-list-create"), 
    path("categ_ingresos/<int:pk>/", CategoriaIngresoRetrieveUpdateDestroy.as_view(), name="categ-ingresos-delete-update-detail"),
    path("ingresos/", IngresoListCreate.as_view(), name="categ-ingresos-list-create"),
    path("ingresos/<int:pk>/", IngresoRetrieveUpdateDestroy.as_view(), name="categ-ingresos-delete-update-detail"),
    path("categ_gastos/", CategoriaGastoListCreate.as_view(), name="categ-gastos-list-create"),
    #     path("categ_gastos/<int:pk>/",
    #          CategoriaIngresoRetrieveUpdateDestroy.as_view(),
    #          name="categ-gastos-delete-update-detail"),
    path("gastos/", GastoListCreate.as_view(), name="categ-gastos-list-create"),

    path("archivazo/comprobante_gasto/<int:pk>/", FileUploadView.as_view()),

    #     path("gastos/<int:pk>/",
    #          IngresoRetrieveUpdateDestroy.as_view(),
    #          name="categ-gastos-delete-update-detail"),
    path('login/', login_view),
    path('logout/', logout_view)
]

# esto es cuando habia hecho dos vistas separadas
# path("ingresos2/", IngresoList.as_view(http_method_names=['get'])),
# path("ingresos/crear/", IngresoCreate.as_view(http_method_names=['post'])),
