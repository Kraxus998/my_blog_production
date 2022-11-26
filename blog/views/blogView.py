import datetime

from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from blog.forms.blogForm import UpdateBlogforms, CreateBlogforms
from blog.forms.loginForm import MyLoginForm
from blog.models.blogModel import Blog
from myblog import settings


class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 5


class BlogDetailView(generic.DetailView):
    model = Blog
    paginate_by = 5


@method_decorator(login_required(login_url=settings.ALTERNATIVE_LOGIN_URL), name="dispatch")
class BlogsByUserListView(generic.ListView):
    model = Blog
    template_name = 'blog/my_blogs_list.html'
    paginate_by = 5

    def get_queryset(self):
        return Blog.objects.filter(blogger__borrower=self.request.user)


class BlogCreate(CreateView):
    model = Blog
    fields = ['title', 'description', 'blogger']
    initial = {
        'post_date': datetime.datetime.now()
    }
    template_name = 'blog/create_blog.html'
    form_class = CreateBlogforms


class BlogUpdate(UpdateView):
    model = Blog
    fields = ['title', 'description', 'post_date',
              'blogger']
    template_name = 'blog/update_blog.html'
    form_class = UpdateBlogforms


@method_decorator(login_required(login_url=settings.LOGIN_URL), name="dispatch")
class BlogDelete(DeleteView):
    model = Blog
    success_url = reverse_lazy('all-blogs')
