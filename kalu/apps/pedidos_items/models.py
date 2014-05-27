from django.db import models
from kalu.apps.pedidos.models import Pedido
from kalu.apps.items.models import Item

# Create your models here.

class Pedido_Item(models.Model):

	pedido = models.ForeignKey(Pedido)
	item = models.ForeignKey(Item)
	cantidad = models.PositiveSmallIntegerField(null=True, default= 0)
	
	def __unicode__(self):
		return unicode(self.pedido)