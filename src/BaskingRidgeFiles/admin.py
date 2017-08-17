from django.contrib import admin

# Register your models here.
from BaskingRidgeFiles.models import gallery_image, menu_entry

admin.site.register(menu_entry)

@admin.register(gallery_image)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('image_tag',)
    readonly_fields = ('image_tag',)