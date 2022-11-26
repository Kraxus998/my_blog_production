from blog.models.bloggerModel import Blogger


def user_blogger_id(request):
    if request.user.is_authenticated:
        blogger = Blogger.objects.filter(borrower=request.user).filter(blog)[0]
    else:
        blogger = None

    return {
        "loged_user_blogger": blogger
    }
