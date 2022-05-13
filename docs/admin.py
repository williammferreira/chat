from django.contrib import admin
from docs.models import Group, Document
from django_summernote.admin import SummernoteModelAdmin

# Register your models here

@admin.register(Group)
class GroupModelAdmin(SummernoteModelAdmin):
	list_display = ('title', 'slug')
	search_fields = ('title',)
	prepopulated_fields = {'slug': ('title',)}
	raw_id_fields = ('parent',)
	exclude = ('id',)


@admin.register(Document)
class DocumentModelAdmin(SummernoteModelAdmin):
	summernote_fields = ('body',)
	list_filter = ('status', 'group')
	list_display = ('title', 'slug')
	search_fields = ('title', 'body')
	prepopulated_fields = {'slug': ('title',)}
	raw_id_fields = ('group',)
	exclude = ('id',)