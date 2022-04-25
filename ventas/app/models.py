from django.db import models
from django.forms import CharField

# Create your models here.
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.FloatField(default= 0)
    
    class Meta:
        db_table = "PRODUCTO"
     