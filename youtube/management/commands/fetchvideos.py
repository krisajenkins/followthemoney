from django.core.management.base		import BaseCommand
import json
import pprint
import urllib
import datetime

from emergency.models					import Emergency, EmergencySearchTerm
from youtube.models						import Video, Channel
from django.db.utils					import IntegrityError

class Command( BaseCommand ):
	help = "TODO"

	def handle( self, *args, **options ):
		pp = pprint.PrettyPrinter()

		for channel in Channel.objects.all():
			author = channel.channel_name

			for search in EmergencySearchTerm.objects.all():
				params   = urllib.urlencode({'author': channel.channel_name, 'alt': 'json', 'q': search.search_term.encode( 'utf8' ), 'max-results': 50})
				feed     = urllib.urlopen( 'http://gdata.youtube.com/feeds/api/videos?%s' % params )
				response = json.loads( feed.read() )

				entries = response['feed'].get('entry', [])

				for entry in entries:
					try:
						( video, created )       = Video.objects.get_or_create(
							youtube_id = entry['id']['$t'],
							defaults = {
								'original_search_term':  search.search_term,
								'emergency':             search.emergency,
								'channel_name':          entry['author'][0]['name']['$t'],
								'description':           entry['content']['$t'],
								'duration':              entry['media$group']['yt$duration']['seconds'],
								'link':                  entry['link'][0]['href'],
								'published':             datetime.datetime.strptime(entry['published']['$t'], "%Y-%m-%dt%H:%M:%S.000z"),
								'title':                 entry['title']['$t'],
								'views':                 entry['yt$statistics']['viewCount'],
								'favourites':            entry['yt$statistics']['favoriteCount'],
							}
						)
					except ( KeyError, ValueError, IntegrityError ):
						pp.pprint( entry['media$group']['yt$duration'] )
						raise

				print "%s -> '%s': Saved %d" % ( author, search.search_term, len( entries ) )
