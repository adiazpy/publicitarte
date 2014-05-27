from django.db import models

# Create your models here.

class Item(models.Model):

	item = models.CharField(max_length=250)
	descripcion = models.CharField(max_length=200)
	precio_unitario = models.PositiveSmallIntegerField(null=True, default= 0)

	def __unicode__(self):
		return unicode(self.item)