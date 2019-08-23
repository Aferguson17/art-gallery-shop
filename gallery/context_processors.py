from .models import Style
def menu_links(request):
    links = Style.objects.all()
    return dict(links=links)