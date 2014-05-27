from django.contrib import admin
from .models import Cliente

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
	list_display = ('nombre','ruc', 'direccion', 'telefono', 'contacto','numero_contacto')
	# list_filter = ('nombre', 'tipo', 'categoria', 'barrio', 'barrio__ciudad')
	search_fields = ('nombre', 'ruc', 'contacto')
	list_display_links = ('nombre',)
	

admin.site.register(Cliente, ClienteAdmin)