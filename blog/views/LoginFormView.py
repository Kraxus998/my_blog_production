from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView

from blog.forms.loginForm import MyLoginForm
from myblog import settings


class BloggerLoginModalView(LoginView):
    model = User
    fields = ['username', 'password']
    template_name = 'registration/my-login-modal.html'
    form_class = MyLoginForm


class BloggerLoginDefaultView(LoginView):
    model = User
    fields = ['username', 'password']
    template_name = 'registration/my-login.html'
    form_class = MyLoginForm


class RemoteLoginView(LoginView):
    model = User
    fields = ['username', 'password']
    template_name = 'registration/login.html'
    form_class = MyLoginForm
    redirect_authenticated_user = True
    redirect_field_name = settings.API_NETWORK_ADMIN_URL
    extra_context = {'redirect_url': settings.API_NETWORK_ADMIN_URL}
