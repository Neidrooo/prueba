from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    # path('<Producto_id>/',views.nombreProducto,name='producto'),
    # path('primera/',views.mostrarTemplate,name='mostrarTemplate'),
    path('mostrar/',views.mostrar,name='mostrar'),
]