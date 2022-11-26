from django.db import models


class ImageFormat(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
