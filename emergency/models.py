from django.db import models
from django.db.models						import Model, Manager, BigIntegerField, ForeignKey, CharField, TextField, ImageField, SlugField, URLField, DateTimeField, Count, permalink, IntegerField

class Emergency( Model ):
	name                = TextField()
	population_affected = BigIntegerField( null = True )
	funds_committed     = BigIntegerField( null = True )

	class Meta:
		ordering = [ 'name' ]
		verbose_name_plural = 'emergencies'

	def __unicode__( self ):
		return self.name

class EmergencySearchTerm( Model ):
	search_term = TextField()
	emergency   = models.ForeignKey( Emergency )

	def __unicode__( self ):
		return self.search_term

