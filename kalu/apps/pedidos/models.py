from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from kalu.apps.clientes.models import Cliente
from kalu.apps.items.models import Item

# Create your models here.

class Pedido(models.Model):

	numero_pedido = models.AutoField(primary_key=True)
	cliente = models.ForeignKey(Cliente)
	#item = models.ManyToManyField('items.Item')
	#cantidad = models.PositiveSmallIntegerField(null=True, default= 0)
	#total = models.PositiveSmallIntegerField(null=True, default= 0)
	fecha_solicitud = models.DateField('Fecha Solicitud', default=datetime.now)
	fecha_aprobacion = models.DateField()
	otros = models.CharField(max_length=200)
	observacion = models.TextField(max_length=400)
	direccion_entrega = models.TextField(max_length=300)
	fecha_entrega = models.DateField()
	facturado = models.BooleanField(default=True)

	def __unicode__(self):
		return unicode(self.cliente.nombre)