from django.contrib import admin
from .models import Pedido_Item
# Register your models here.

class Pedido_ItemAdmin(admin.ModelAdmin):
	list_display = ('cantidad','pedido', 'item')
	# list_filter = ('nombre', 'tipo', 'categoria', 'barrio', 'barrio__ciudad')
	#search_fields = ('item')
	#list_display_links = ('item',)
	

admin.site.register(Pedido_Item, Pedido_ItemAdmin)