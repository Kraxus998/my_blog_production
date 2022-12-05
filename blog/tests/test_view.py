# Create your tests here.

from django.test import TestCase
from django.urls import reverse

from blog.models.bloggerModel import Blogger
from blog.models.imageFormatModel import ImageFormat
from blog.models.imageModel import Image
from django.contrib.auth.models import User


# Create your tests here.
class BLogListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(
            username='testing',
            password='testing'
        )
        iformat = ImageFormat.objects.create(
            name='jpg'
        )
        image = Image.objects.create(
            name='testing_image',
            format=iformat,
            route='/images'
        )
        # Create 5 blog for pagination tests
        number_of_bloggers = 10
        for blogger_num in range(number_of_bloggers):
            Blogger.objects.create(
                username=f'{user.username}_user#{blogger_num}',
                bio=f'soy{user.username}_user#{blogger_num}',
                image=image,
                borrower=user
            )

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/all-bloggers/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('all-bloggers'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('all-bloggers'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'blog/blogger_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('all-bloggers'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['blogger_list']) == 4)

    def test_lists_all_authors(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        resp = self.client.get(reverse('all-bloggers') + '?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['blogger_list']) == 4)
