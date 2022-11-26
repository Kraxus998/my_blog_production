from django.contrib import admin

from blog.models.blogCommentModel import BlogComment
from blog.models.blogModel import Blog
from blog.models.bloggerModel import Blogger

# Register your models here.
from blog.models.imageFormatModel import ImageFormat
from blog.models.imageModel import Image

admin.site.register(Blog)
admin.site.register(Blogger)
admin.site.register(BlogComment)
admin.site.register(Image)
admin.site.register(ImageFormat)
