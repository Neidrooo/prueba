from django.urls import path
from . import views

app_name='app'
urlpatterns = [
    path('',views.index,name='index'),
    # path('<Producto_id>/',views.nombreProducto,name='producto'),
    # path('primera/',views.mostrarTemplate,name='mostrarTemplate'),
    path('mostrar/',views.mostrar,name='mostrar'),
    path('errores/',views.errores,name='errores'),
    path('<int:id>/entrada/',views.entrada,name='entrada'),
    path('<int:id>/entrada_error/',views.entrada_error,name='entrada_error'),
    path('mostrar_subconjunto/',views.mostrar_subconjunto,name='mostrar_subconjunto'),
    path('formulario/',views.formulario,name='formulario'),
    path('elegir_vistas/',views.elegir_vistas,name='elegir_vistas'),
    path('<str:nombre>/guardar_bd/',views.guardar_bd,name='guardar_bd'),
]