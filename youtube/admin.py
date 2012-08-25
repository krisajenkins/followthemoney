from django.contrib							import admin

from youtube.models							import Video

class VideoAdmin( admin.ModelAdmin ):
	list_display			= ( 'author_name', 'description', 'duration', 'link' )

admin.site.register( Video, VideoAdmin )
