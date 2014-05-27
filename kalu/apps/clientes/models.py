from django.db import models

# Create your models here.

class Cliente(models.Model):

	nombre = models.CharField(max_length=200)
	ruc = models.CharField(max_length=250)
	direccion = models.CharField(max_length=500)
	telefono = models.CharField(max_length=250)
	contacto = models.CharField(max_length=250)
	numero_contacto = models.CharField(max_length=250)

	def __unicode__(self):
		return unicode(self.nombre)

