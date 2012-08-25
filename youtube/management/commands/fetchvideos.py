from django.core.management.base		import BaseCommand
import json
import pprint
import urllib

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
			author_name = entry['author'][0]['name']['$t']
			description = entry['content']['$t']
			duration = entry['media$group']['yt$duration']['seconds']
			link = entry['link'][0]['href']

			video = Video( author_name = author_name, description = description, duration = duration, search_term = search_term, link = link )
			video.save()

		print "Saved"
