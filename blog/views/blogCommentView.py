from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.utils.decorators import method_decorator
from django.views import generic

from blog.models.blogCommentModel import BlogComment
from myblog import settings


class CommentsListView(PermissionRequiredMixin, generic.ListView):
    model = BlogComment
    context_object_name = 'comments_list'
    template_name = 'blog/comments_list.html'
    paginate_by = 3
    permission_required = 'is_staff'

    def get_queryset(self):
        return BlogComment.objects.all()


@method_decorator(login_required(login_url=settings.ALTERNATIVE_LOGIN_URL), name='dispatch')
class CommentsByUserListView(generic.ListView):
    model = BlogComment
    context_object_name = 'my_comments_list'
    template_name = 'blog/my_comments_list.html'
    paginate_by = 3

    def get_queryset(self):
        return BlogComment.objects.filter(blogger__borrower=self.request.user)
