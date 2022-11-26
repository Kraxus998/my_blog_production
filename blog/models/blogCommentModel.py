import uuid

from django.db import models
from django.urls import reverse

from blog.models.blogModel import Blog
from blog.models.bloggerModel import Blogger
from blog.permissions.bloggerPermissions import PERMISSIONS as BLOGGER_PERMISSIONS


class BlogComment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Unique ID for this particular Comment across whole Blogs')
    post_date = models.DateTimeField(null=True, blank=True)
    description = models.TextField(max_length=255, blank=False)
    blog = models.ForeignKey(Blog, on_delete=models.DO_NOTHING)
    blogger = models.ForeignKey(Blogger, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ['-post_date']
        permissions = BLOGGER_PERMISSIONS

    def __str__(self):
        return f'{self.blogger}({self.post_date})-{self.description}'

    def get_absolute_url(self):
        return reverse('blogcomment-detail', args=[str(self.id)])
