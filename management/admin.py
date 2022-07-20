from django.contrib import admin
from .models import App, AppGroup

# Register your models here.


@admin.register(AppGroup)
class AppGroupAdmin(admin.ModelAdmin):
    '''Admin View for AppGroup'''

    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost_monthely')
    search_fields = ('name', 'cost_monthely', 'cost_yearly')
    ordering = ('name',)
