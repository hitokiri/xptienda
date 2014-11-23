from django.db import models

class CategoriasProducto(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.TextField(max_length=500)
	class Meta:
		verbose_name = "CategoriasProducto"
        verbose_name_plural = "CategoriasProductos"

	def __str__(self):
		return self.nombre

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
	categorias = models.ManyToManyField(CategoriasProducto)

	class Meta:
		verbose_name = "Producto"
		verbose_name_plural = "Productos"
		
	def __unicode__(self):
			return self.nombre

class Oferta(models.Model):
	producto = models.CharField(max_length=50)
	precio = models.DecimalField(max_digits=5, decimal_places=2)
	fecha = models.DateField(auto_now_add=True)
	fecha_inicio=models.DateField(auto_now=True)
	fecha_final=models.DateField()

	class Meta:
		verbose_name = "Oferta"
		verbose_name_plural = "Ofertas"
		
	def __unicode__(self):
			return self.producto
class Boletin(models.Model):
	archivo = models.FileField(upload_to=nombre_modificar)
	descripcion = models.TextField(max_length=900)
	fecha = models.DateField(auto_now_add=True)

	class Meta:
		verbose_name = "Boletin"
		verbose_name_plural = "Boletines"
		
	def __unicode__(self):
			return self.tipo

class Evento(models.Model):
	descripcion = models.TextField(max_length=900)
	fecha = models.DateField(auto_now_add=True)
	fecha_inicio=models.DateField(auto_now_add=True)
	fecha_final=models.DateField()

	class Meta:
		verbose_name = "Evento"
		verbose_name_plural = "Eventos"
		
	def __unicode__(self):
			return self.descripcion

class Suscriptor(models.Model):
	activo = models.BooleanField(default=True)
	email = models.EmailField(max_length=254)
	fecha = models.DateField(auto_now_add=True)
	
	class Meta:
		verbose_name = "Suscriptor"
		verbose_name_plural = "Suscriptores"
		
	def __unicode__(self):
			return self.nombre