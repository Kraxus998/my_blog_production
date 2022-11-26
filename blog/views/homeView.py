import datetime
from http.client import HTTPResponse

from django.shortcuts import render, redirect
from django.views import generic

from blog.models.blogCommentModel import BlogComment
from blog.models.blogModel import Blog
from blog.models.bloggerModel import Blogger
from myblog import settings


def indexView(request):
    num_bloggers = Blogger.objects.count()
    num_blogs = Blog.objects.count()
    num_comments = BlogComment.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'date': datetime.date.today(),
        'num_bloggers': num_bloggers,
        'num_blogs': num_blogs,
        'num_comments': num_comments,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context=context)


class ApiView(generic.View):
    @staticmethod
    def apiNetworkView(request):
        # context = {
        #     "address": "",
        #     "CIDR": "null",
        #     "inUse": "false",
        #     "userId": "",
        #     "projectId": "",
        #     "projectName": "",
        #     "username": "",
        #     "domain": ""
        # }
        return redirect(to=f'{settings.API_NETWORK_ADMIN_URL}')
