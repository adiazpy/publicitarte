from django.contrib import admin
from .models import Pedido_Item


# Register your models here.

class Pedido_ItemAdmin(admin.ModelAdmin):
	
	list_display = ('numero_pedido', 'cliente_nombre', 'fecha_solicitud', 'fecha_aprobacion', 'fecha_entrega','item', 'descripcion', 'precio_unitario')
	#list_display = ('cantidad','pedido', 'item')
	# list_filter = ('nombre', 'tipo', 'categoria', 'barrio', 'barrio__ciudad')
	#search_fields = ('item')
	#list_display_links = ('item',)
	

	def numero_pedido(self, obj):
		return obj.pedido.numero_pedido

	def cliente_nombre(self, obj):
		return obj.pedido.cliente.nombre

	def fecha_solicitud(self, obj):
		return obj.pedido.fecha_solicitud

	def fecha_aprobacion(self, obj):
		return obj.pedido.fecha_aprobacion

	def fecha_entrega(self, obj):
		return obj.pedido.fecha_entrega

	def item(self, obj):
		return obj.item.item

	def descripcion(self, obj):
		return obj.item.descripcion

	def precio_unitario(self, obj):
		return obj.item.precio_unitario

admin.site.register(Pedido_Item, Pedido_ItemAdmin)

