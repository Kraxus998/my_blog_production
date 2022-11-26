import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from blog.forms.blogForm import UpdateBlogforms, CreateBlogforms
from blog.models.blogModel import Blog
from blog.models.bloggerModel import Blogger
from myblog import settings


@login_required(login_url=settings.LOGIN_URL)
# @permission_required('blog.', raise_exception=True)
def update_Blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = UpdateBlogforms(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            blog.title = form.cleaned_data['title']
            blog.post_date = form.cleaned_data['post_date']
            blog.description = form.cleaned_data['description']
            blog.blogger = form.cleaned_data['blogger']
            blog.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-blogs'))

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_title = 'Your New Title'
        proposed_post_date = datetime.datetime.now()
        proposed_description = 'a brieve description'
        proposed_blogger = None

        form = UpdateBlogforms(
            initial={
                "title": proposed_title,
                "post_date": proposed_post_date,
                "description": proposed_description,
                "blogger": proposed_blogger,
            }
        )

        context = {
            'form': form,
            'blog': blog,
        }

        return render(request, 'blog/update_blog.html', context)


@login_required(login_url=settings.LOGIN_URL)
def create_Blog(request):
    blog = Blog()
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = CreateBlogforms(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            blog.title = form.cleaned_data['title']
            blog.post_date = datetime.datetime.now()
            blog.description = form.cleaned_data['description']
            blog.blogger = form.cleaned_data['blogger']
            blog.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-blogs'))

        # If this is a GET (or any other method) create the default form.
    else:
        proposed_title = 'Title'
        proposed_post_date = datetime.datetime.now()
        proposed_description = 'a brieve description'
        # proposed_blogger = Blogger.objects.filter(borrower=request.user)
        proposed_blogger = None

        form = CreateBlogforms(
            initial={
                "title": proposed_title,
                "post_date": proposed_post_date,
                "description": proposed_description,
                "blogger": proposed_blogger,
            }
        )

    context = {
        'form': form,
        'blog': blog,
        'date': proposed_post_date,
    }

    return render(request, 'blog/create_blog.html', context)
