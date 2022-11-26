from django.shortcuts import render

from django.views import generic

from blog.models.bloggerModel import Blogger


class BloggerListView(generic.ListView):
    model = Blogger
    paginate_by = 4


class BloggerDetailView(generic.DetailView):
    model = Blogger
    paginate_by = 4
