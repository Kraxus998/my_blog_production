from django.test import TestCase

from blog.models.imageFormatModel import ImageFormat
from blog.models.imageModel import Image


class ImageFormatModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        ImageFormat.objects.create(name='jpg')

    def test_name_label(self):
        image_fomat = ImageFormat.objects.get(id=1)
        field_label = image_fomat._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')


class ImageModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        format = ImageFormat.objects.create(name='jpg')
        image = Image.objects.create(
            name='test',
            route='/images',
            format=format,
        )

    def test_name_label(self):
        image = Image.objects.get(id=1)
        field_label = image._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')
