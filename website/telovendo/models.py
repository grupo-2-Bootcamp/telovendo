from django.db import models

# Create your models here.
class FormularioProveedoresDB(models.Model):
    nombre_proveedor = models.CharField (max_length=50,   null=False, blank=False)
    razon_social     = models.CharField (max_length=50,   null=False, blank=False)
    rut              = models.CharField (max_length=12,   null=False, blank=False)
    giro             = models.CharField (max_length=30,   null=False, blank=False)
    contacto         = models.CharField (max_length=30,   null=False, blank=False)
    telefono         = models.CharField (max_length=30,   null=False, blank=False)
    email            = models.EmailField(max_length=30,   null=False, blank=False)
    direccion        = models.CharField (max_length=30,   null=False, blank=False) 
    comuna           = models.CharField (max_length=20,   null=False, blank=False)
    categoria        = models.CharField (max_length=30,   null=False, blank=False)
    productos        = models.CharField (max_length=1000, null=False, blank=False)


class ConsultaProveedor(models.Model):
    proveedor = models.CharField(max_length=100, null=False, blank=False)
    asunto = models.CharField(max_length=200, null=False, blank=False)
    mensaje = models.TextField(null=False, blank=False)