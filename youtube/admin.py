from django.contrib							import admin

from youtube.models							import Video

class VideoAdmin( admin.ModelAdmin ):
	list_display = ( 'youtube_id', 'author_name', 'title', 'description', 'duration', 'link', 'search_term', 'published', 'views', 'favourites' )

admin.site.register( Video, VideoAdmin )
