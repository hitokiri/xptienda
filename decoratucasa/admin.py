from django.contrib import admin
from .models import Producto, Oferta, Boletin, Evento, Suscriptor, CategoriasProducto

# Register your models here.
admin.site.register(Producto)
admin.site.register(Boletin)
admin.site.register(Evento)
admin.site.register(Oferta)
admin.site.register(Suscriptor)
admin.site.register(CategoriasProducto)