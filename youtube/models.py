from django.db import models
from django.db.models						import Model, Manager, ForeignKey, CharField, TextField, ImageField, SlugField, URLField, DateTimeField, Count, permalink, IntegerField

class Video( Model ):
	author_name	= CharField( max_length = 200 )
	description	= CharField( max_length = 500 )
	duration	= IntegerField()
	search_term	= CharField( max_length = 100 )
	link		= URLField()

	class Meta:
		ordering = [ '-author_name', '-duration' ]

	def __unicode__( self ):
		return self.link
