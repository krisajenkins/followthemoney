from django.core.management.base		import BaseCommand
import json
import pprint
import urllib
import datetime

from youtube.models						import Video

class Command( BaseCommand ):
	args = "<channel_id> '<search terms>'"
	help = "TODO"

	def handle( self, *args, **options ):
		author = args[0]
		search_term  = args[1]

		params = urllib.urlencode({'author': author, 'alt': 'json', 'q': search_term, 'max-results': 50})
		f = urllib.urlopen( 'http://gdata.youtube.com/feeds/api/videos?%s' % params )
		obj = json.loads( f.read() )

		pp = pprint.PrettyPrinter()
		# pp.pprint( entries[0] )
		entries = obj['feed']['entry']

		print author
		print search_term

		for entry in entries:
			video = Video()
			
			video.youtube_id  = entry['id']['$t']
			video.search_term = search_term
			video.author_name = entry['author'][0]['name']['$t']
			video.description = entry['content']['$t']
			video.duration    = entry['media$group']['yt$duration']['seconds']
			video.link        = entry['link'][0]['href']
			video.published   = datetime.datetime.strptime(entry['published']['$t'], "%Y-%m-%dT%H:%M:%S.000Z")
			video.title       = entry['title']['$t']
			video.views       = entry['yt$statistics']['viewCount']
			video.favourites  = entry['yt$statistics']['favoriteCount']

			video.save()

		print "Saved %d" % len( entries )
