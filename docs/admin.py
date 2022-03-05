from django.contrib import admin
from docs.models import Group, Document
from django_summernote.admin import SummernoteModelAdmin

# Register your models here

class GroupAndDocumentModelAdmin(SummernoteModelAdmin):
	summernote_fields = ('content')
	list_display = ('name', 'slug')

admin.site.register(Group, GroupAndDocumentModelAdmin)
admin.site.register(Document, GroupAndDocumentModelAdmin)