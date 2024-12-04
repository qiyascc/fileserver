from django.contrib import admin
from .models import FileType, File

class FileInline(admin.TabularInline):
    model = File
    extra = 1

@admin.register(FileType)
class FileTypeAdmin(admin.ModelAdmin):
    inlines = [FileInline]

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('name', 'file_type', 'upload_date')
