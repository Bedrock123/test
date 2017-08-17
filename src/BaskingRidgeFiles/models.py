from __future__ import unicode_literals
from filer.fields.image import FilerImageField, FilerFileField
from django.utils.html import mark_safe
from django.db import models

# Create your models here.
class gallery_image(models.Model):

    image = FilerImageField(null=True, blank=False,
                           related_name="gallery_image")
    def __unicode__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Gallery Image'
        verbose_name_plural = 'Gallery Images'

    def image_tag(self):
        return mark_safe('<img src="%s" width=155/>' % (self.image.url))

class menu_entry(models.Model):
    menu_name = models.CharField(max_length=255, blank=False)
    menu_pdf = FilerFileField(null=True, blank=False,
                           related_name="menu_pdfs")
    description = models.TextField(
        'Menu Description',
        blank=True,
        null=True
    )
    
    def __unicode__(self):
        return self.menu_name


    class Meta:
        verbose_name = 'Menu Entry'
        verbose_name_plural = 'Menu Entries'

