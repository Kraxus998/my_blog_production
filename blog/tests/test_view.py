# Create your tests here.

import datetime
import random
from random import randint

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from blog.models.blogCommentModel import BlogComment
from blog.models.blogModel import Blog
from blog.models.bloggerModel import Blogger
from blog.models.imageFormatModel import ImageFormat
from blog.models.imageModel import Image


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

    def test_pagination_is_four(self):
        resp = self.client.get(reverse('all-bloggers'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['blogger_list']) == 4)

    def test_lists_all_bloggers(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        resp = self.client.get(reverse('all-bloggers') + '?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['blogger_list']) == 4)


class CommentsListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create two users one of them with staff permission
        test_user = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user_admin = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD', is_staff=True,
                                                   is_superuser=True)

        test_user.save()
        test_user_admin.save()

        # Create a image format
        iformat = ImageFormat.objects.create(
            name='jpg'
        )
        # Create a image
        image = Image.objects.create(
            name='testing_image',
            format=iformat,
            route='/images'
        )

        # Create 2 blogers for permissions tests
        blogger = Blogger.objects.create(
            username=f'{test_user.username}_user#{test_user.id}',
            bio=f'soy {test_user.username}_user#{test_user.id}',
            image=image,
            borrower=test_user
        )
        blogger_admin = Blogger.objects.create(
            username=f'{test_user_admin.username}_user#{test_user_admin.id}',
            bio=f'soy {test_user_admin.username}_user#{test_user_admin.id}',
            image=image,
            borrower=test_user_admin
        )

        blogger.save()
        blogger_admin.save()

        test_blogger_list = [blogger, blogger_admin]

        # Create Blogs for each blogger
        blog_1 = Blog.objects.create(
            post_date=datetime.datetime.now(),
            blogger=blogger,
            title='Testing Blog 1',
            description='A brieve description'
        )
        blog_2 = Blog.objects.create(
            post_date=datetime.datetime.now(),
            blogger=blogger,
            title='Testing Blog 2',
            description='A brieve description'
        )
        blog_1.save()
        blog_2.save()

        test_blog_list = [blog_1, blog_2]

        # Create some comments for each blog
        for i in range(1, randint(2, 30)):
            choice_blog = random.choice(test_blog_list)
            choice_blogger = random.choice(test_blogger_list)
            BlogComment.objects.create(
                post_date=datetime.datetime.now(),
                description=f'soy el comentario de {choice_blog}',
                blogger=choice_blogger,
                blog=choice_blog
            )

    def test_all_comments_section_visibility_false_if_not_is_staff(self):
        # loging in user 1
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('all-comments'))

        # Check our user is logged in
        # self.assertEqual(str(response.context['user']), 'testuser1')

        # Check that we got a correct response "Forbiden"
        self.assertEqual(response.status_code, 403)

        # loging in user 2
        logout = self.client.logout()
        login = self.client.login(username='testuser2', password='2HJ1vRV0Z&3iD')
        response = self.client.get(reverse('all-comments'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser2')

        # Check that we got a correct response "Forbiden"
        self.assertEqual(response.status_code, 200)

    def test_my_comments_list_view(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('my-comments'))
        lista = response.context['my_comments_list']
        owner_of_all_comments_in_list = True

        # Verify that the actual user have no comments
        if response.context['my_comments_list'] is None and response.context['user'] == 'testuser1':
            self.assertTrue(owner_of_all_comments_in_list)

        else:
            # Assigns False to the Flag if the user is not owner of one comment in the list
            for comment in response.context['my_comments_list']:
                if not comment.blogger.borrower == response.context['user']:
                    owner_of_all_comments_in_list = False
                    self.assertTrue(owner_of_all_comments_in_list)
