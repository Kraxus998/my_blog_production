from blog import urls


def urlpatterns(request):
    my_urls = urls.urlpatterns
    clean_urls = []
    exclude_urls = ['create', 'update', 'delete', 'login', 'register']

    for url in my_urls:
        add = True
        for i in clean_urls:
            if url.name == i.name:
                add = False
            elif exclude_urls[0] in url.name or exclude_urls[1] in url.name \
                    or exclude_urls[2] in url.name \
                    or exclude_urls[3] in url.name or exclude_urls[4] in url.name:
                add = False
        if add:
            clean_urls.append(url)
    return {
        "urlpatterns": clean_urls
    }
