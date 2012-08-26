from django.conf					import settings
from django.contrib.sites.models	import Site
from django.core.urlresolvers		import reverse
from django.views.generic			import ListView, TemplateView
from django.db.models				import Avg, Sum

from emergency.models				import Emergency
from youtube.models					import Video

class MainReportView( ListView ):
	queryset = Video.objects.values("emergency__name", "emergency__people_affected", "emergency__funds_committed").annotate( total_duration = Sum( 'duration' ) ).order_by( "emergency__name" )
