from django.contrib							import admin

from emergency.models						import Emergency, EmergencySearchTerm

class EmergencyAdmin( admin.ModelAdmin ):
	list_display = (
		'name',
		'people_affected',
		'people_died',
		'people_injured',
		'people_missing',
		'people_displaced',
		'funds_committed',
	)

class EmergencySearchTermAdmin( admin.ModelAdmin ):
	list_display = (
		'emergency',
		'search_term',
	)

admin.site.register( Emergency, EmergencyAdmin )
admin.site.register( EmergencySearchTerm, EmergencySearchTermAdmin )
