from django.contrib import admin
from .models import Concept


class ConceptAdmin(admin.ModelAdmin):
	pass
admin.site.register(Concept, ConceptAdmin)