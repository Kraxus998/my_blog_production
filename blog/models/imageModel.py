from django.db import models

from blog.models.imageFormatModel import ImageFormat


class Image(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    route = models.CharField(max_length=255, blank=True, null=True, default='/images')
    format = models.ForeignKey(ImageFormat, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ['route']

    def __str__(self):
        return f'{self.route}/{self.name}.{self.format}'
