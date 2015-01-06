from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from reversion import VersionAdmin
from .models import *

@admin.register(Pool)
class PoolAdmin(VersionAdmin, admin.ModelAdmin):
	list_display = ['created_at', 'name', 'start_date', 'end_date']
	list_filter = ['start_date', 'end_date']
	search_fields = ['name']

@admin.register(Post)
class PostAdmin(VersionAdmin, AdminImageMixin, admin.ModelAdmin):
	list_display = ['created_at', 'pool', 'description', 'signature', 'width', 'height']
	list_filter = ['pool__name', 'created_at']
	search_fields = ['created_at', 'pool__name', 'description', 'signature']
	readonly_fields = ['width', 'height']
