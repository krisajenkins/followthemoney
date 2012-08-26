from django.conf.urls			import patterns, include, url

from django.contrib import admin
from django.views.generic.simple	import direct_to_template

from followthemoney.views			import MainReportView

admin.autodiscover()

urlpatterns = patterns('',
	# Admin.
	url( r'^admin/doc/',							include( 'django.contrib.admindocs.urls' ) ),
	url( r'^admin/',								include( admin.site.urls ) ),

	url( r'^stats.csv',								MainReportView.as_view(), name = 'main_report' ),
	url( r'^$',										direct_to_template, {'template': 'index.html' } ),
)
