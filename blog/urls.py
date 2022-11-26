from django.urls import path, re_path

from .views import homeView
from .views.LoginFormView import BloggerLoginDefaultView, BloggerLoginModalView, RemoteLoginView
from .views.blogCommentView import CommentsByUserListView, CommentsListView
from .views.blogFormView import update_Blog, create_Blog
from .views.blogView import BlogListView, BlogDetailView, BlogsByUserListView, BlogCreate, BlogUpdate, BlogDelete
from .views.bloggerView import BloggerListView, BloggerDetailView
from .views.registerFormView import my_register, register_success

urlpatterns = [
    # Home urls
    path(route='home/', view=homeView.indexView, name='home'),
    path(route='', view=homeView.indexView, name='home'),
    path(route='api-network/', view=homeView.ApiView.apiNetworkView, name='api-network'),
    path(route='my-login/', view=BloggerLoginDefaultView.as_view(), name='my-login'),
    path(route='remote-login/', view=RemoteLoginView.as_view(), name='remote-login'),
    path(route='my-login-modal/', view=BloggerLoginModalView.as_view(), name='my-login-modal'),
    path(route='my-register-modal/', view=my_register, name='my-register-modal'),
    path(route='register-success/', view=register_success, name='register-success'),
    # List and Details actions
    # --Start--
    path('all-bloggers/', BloggerListView.as_view(), name='all-bloggers'),
    path('all-bloggers/<int:pk>', BloggerDetailView.as_view(), name='all-bloggers'),
    path('all-blogs/', BlogListView.as_view(), name='all-blogs'),
    path('all-blogs/<int:pk>', BlogDetailView.as_view(), name='all-blogs'),
    path('my-blogs/', BlogsByUserListView.as_view(), name='my-blogs'),
    path('my-comments/', CommentsByUserListView.as_view(), name='my-comments'),
    path('all-comments/', CommentsListView.as_view(), name='all-comments'),
    # --End--
    # Create, Update, Delete actions
    # --Start--
    path('all-blogs/create-blog/', create_Blog, name='create-blog'),
    path('all-blogs/<int:pk>/update-blog/', update_Blog, name='update-blog'),
    path('all-blogs/<int:pk>/delete-blog/', BlogDelete.as_view(), name='delete-blog'),
    # --End--
]
