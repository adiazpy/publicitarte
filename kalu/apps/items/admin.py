from django.contrib import admin
from .models import Item

# Register your models here.

class ItemAdmin(admin.ModelAdmin):
	list_display = ('item','descripcion', 'precio_unitario')
	# list_filter = ('nombre', 'tipo', 'categoria', 'barrio', 'barrio__ciudad')
	#search_fields = ('item')
	list_display_links = ('item',)
	

admin.site.register(Item, ItemAdmin)