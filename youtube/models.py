from django.db import models
from django.db.models						import Model, Manager, ForeignKey, CharField, TextField, ImageField, SlugField, URLField, DateTimeField, Count, permalink, IntegerField

from emergency.models						import Emergency

class Video( Model ):
	youtube_id           = TextField( unique = True )
	channel_name         = TextField()
	description          = TextField()
	duration             = IntegerField()
	title                = TextField()
	original_search_term = TextField()
	link                 = URLField()
	published            = DateTimeField()
	views                = IntegerField()
	favourites           = IntegerField()
	emergency            = models.ForeignKey( Emergency )

	class Meta:
		ordering = [ '-channel_name', '-duration' ]

	def __unicode__( self ):
		return "title=%s, duration=%s" % ( self.title, self.duration )

class Channel( Model ):
	channel_name = TextField( primary_key = True )

	class Meta:
		ordering = [ 'channel_name' ]

	def __unicode__( self ):
		return self.channel_name
