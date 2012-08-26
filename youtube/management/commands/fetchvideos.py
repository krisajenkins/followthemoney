from django.core.management.base		import BaseCommand
import json
import pprint
import urllib
import datetime

from emergency.models					import Emergency, EmergencySearchTerm
from youtube.models						import Video, Channel

class Command( BaseCommand ):
	help = "TODO"

	def handle( self, *args, **options ):
		pp = pprint.PrettyPrinter()

		for channel in Channel.objects.all():
			author = channel.channel_name

			for search in EmergencySearchTerm.objects.all():
				params   = urllib.urlencode({'author': channel.channel_name, 'alt': 'json', 'q': search.search_term, 'max-results': 50})
				feed     = urllib.urlopen( 'http://gdata.youtube.com/feeds/api/videos?%s' % params )
				response = json.loads( feed.read() )


				entries = response['feed'].get('entry', [])

				for entry in entries:
					( video, created )       = Video.objects.get_or_create(
						youtube_id           = entry['id']['$t'],
						original_search_term = search.search_term,
						emergency            = search.emergency,
						channel_name         = entry['author'][0]['name']['$t'],
						description          = entry['content']['$t'],
						duration             = entry['media$group']['yt$duration']['seconds'],
						link                 = entry['link'][0]['href'],
						published            = datetime.datetime.strptime(entry['published']['$t'], "%Y-%m-%dT%H:%M:%S.000Z"),
						title                = entry['title']['$t'],
						views                = entry['yt$statistics']['viewCount'],
						favourites           = entry['yt$statistics']['favoriteCount'],
					)

					video.save()

				print "%s -> '%s': Saved %d" % ( author, search.search_term, len( entries ) )
