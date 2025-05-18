from django.contrib import admin

from documents import models
# Register your models here.

@admin.register(models.Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("name","upload_at","size","content_type")
    search_fields = ("name","content_type")
    ordering = ("upload_at",)
