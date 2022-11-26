from django.db import models
from django.urls import reverse

from blog.models.bloggerModel import Blogger


class Blog(models.Model):
    title = models.CharField(max_length=255, blank=False)
    post_date = models.DateField(blank=True, null=True)
    description = models.TextField(max_length=255, blank=False)
    blogger = models.ForeignKey(Blogger, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ['-post_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('all-blogs', args=[str(self.id)])
