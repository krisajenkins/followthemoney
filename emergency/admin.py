from django.contrib							import admin

from emergency.models						import Emergency, EmergencySearchTerm

class EmergencyAdmin( admin.ModelAdmin ):
	pass

class EmergencySearchTermAdmin( admin.ModelAdmin ):
	pass

admin.site.register( Emergency, EmergencyAdmin )
admin.site.register( EmergencySearchTerm, EmergencySearchTermAdmin )
