from django.contrib import admin
from .models import Pedido

# Register your models here.

class PedidoAdmin(admin.ModelAdmin):
	list_display = ('numero_pedido', 'cliente', 'fecha_solicitud', 'fecha_aprobacion', 'fecha_entrega', 'facturado')
	# list_filter = ('nombre', 'tipo', 'categoria', 'barrio', 'barrio__ciudad')
	search_fields = ('numero_pedido', 'cliente')
	list_display_links = ('numero_pedido',)
	#filter_horizontal = ('item', )


admin.site.register(Pedido, PedidoAdmin)