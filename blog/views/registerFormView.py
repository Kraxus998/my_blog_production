from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from blog.forms.loginForm import MyRegisterForm


def my_register(request):
    if request.method == 'POST':
        form = MyRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register-success')
    else:
        form = MyRegisterForm()
    context = {
        'form': form
    }
    return render(request, 'registration/my-register-modal.html', context)


def register_success(request):
    return render(request, 'registration/register-success.html')
