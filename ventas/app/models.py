from django.db import models

# Create your models here.



class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table='CATEGORIA'

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.FloatField(default= 0)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    class Meta:
        db_table = "PRODUCTO"

