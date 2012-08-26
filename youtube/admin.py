from django.contrib							import admin

from youtube.models							import Video, Channel

class VideoAdmin( admin.ModelAdmin ):
	list_display = (
		'emergency',
		'channel_name',
		'title',
		'description',
		'duration',
		'views',
		'favourites',
		'published',
		'link',
	)

class ChannelAdmin( admin.ModelAdmin ):
	list_display = ( 'channel_name', )

admin.site.register( Video, VideoAdmin )
admin.site.register( Channel, ChannelAdmin )
