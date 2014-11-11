from django.db import models

# Create your models here.
class Producto(models.Model):
	nombre = models.CharField(max_length=50)
	precio = models.DecimalField(max_digits=5, decimal_places=2)
	cantidad = models.IntegerField()
	fecha = models.DateTimeField(auto_now_add=True)
	class Meta:
		verbose_name = "Producto"
		verbose_name_plural = "Productos"
		
	def __unicode__(self):
			return self.nombre

