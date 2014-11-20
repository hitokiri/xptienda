from django.db import models


def nombre_modificar(instance, filename):
    nombre = filename.replace(' ', '_')
    formato = 'producto/imagenes/%s' % (nombre)
    return formato

# Create your models here.
class Producto(models.Model):
	nombre = models.CharField(max_length=50)
	precio = models.DecimalField(max_digits=5, decimal_places=2)
	cantidad = models.IntegerField()
	fecha = models.DateTimeField(auto_now_add=True)
	descripcion = models.TextField(max_length=900)
	imagen = models.ImageField(upload_to=nombre_modificar)

	class Meta:
		verbose_name = "Producto"
		verbose_name_plural = "Productos"
		
	def __unicode__(self):
			return self.nombre
