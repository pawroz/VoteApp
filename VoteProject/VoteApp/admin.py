from django.contrib import admin

from .models import *

admin.site.site_header = 'Aviva Poznań Północ'
admin.site.site_title = 'Admin'
admin.site.index_title = 'Aviva Poznań Północ'

class ChoiceInLine(admin.TabularInline):
	model = Choice
	extra = 3


class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [(None, {'fields': ['question']}), 
				('Date Information', {'fields':['pub_date'], 'classes': ['collapse']}),
	]

	inlines = [ChoiceInLine]

# admin.site.register(Question)
# admin.site.register(Choice)

admin.site.register(Question, QuestionAdmin)