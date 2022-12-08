from django.db import models




# Create your models here.
class TipoProducto(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_producto = models.CharField(max_length=30,  blank=True, null=True)
    def __str__(self):
        return self.tipo_producto
class distribuidor(models.Model):
    distribuidor_id = models.AutoField(primary_key=True)
    distribuidor_name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.distribuidor_name
class marca(models.Model):
    marca_id = models.AutoField(primary_key=True)
    marca_name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.marca_name
class tipo2(models.Model):
    tipo2_id = models.AutoField(primary_key=True)
    tipo2_name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.tipo2_name
class productos(models.Model):
    id = models.AutoField(primary_key=True)
    producto = models.CharField(max_length=25, verbose_name='producto', blank=True, null=True)
    precio_entrada = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Valor entrada', blank=True, null=True)
    precio_salida = models.IntegerField(verbose_name='Precio de venta', blank=True, null=True)
    fecha_vencimiento = models.DateField(verbose_name='Fecha de Vencimiento', blank=True, null=True)
    Distribuidor = models.ForeignKey('distribuidor', on_delete=models.CASCADE, blank=True, null=True)
    Marca = models.ForeignKey('marca', on_delete=models.CASCADE, blank=True, null=True)
    facturas = models.CharField(max_length=25, verbose_name='Facturas', blank=True, null=True)
    cantidad = models.IntegerField(verbose_name='Cantidad', blank=True, null=True)
    activo= models.BooleanField(max_length=50, default='True')
    tipo = models.ManyToManyField(TipoProducto)
    Tipo2 = models.ForeignKey('tipo2', on_delete=models.CASCADE, blank=True, null=True)
    
    




    





    
    