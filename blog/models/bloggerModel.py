from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from blog.models.imageModel import Image


class Blogger(models.Model):
    username = models.CharField(max_length=255, blank=False)
    bio = models.CharField(max_length=255, blank=False)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, blank=True, null=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['username']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('all-bloggers', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.borrower.username
