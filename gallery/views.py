from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Style, Painting

def index(request):
    text_var = 'Ferguson Art Gallery Shop'
    return HttpResponse(text_var)    

def allPaintSty(request, s_slug=None):
    s_page = None
    paintings = None
    if s_slug!=None:
        s_page = get_object_or_404(Style,slug=s_slug)
        paintings = Painting.objects.filter(style=s_page,available=True)
    else: 
      paintings = Painting.objects.all().filter(available=True) 
    return render(request,'gallery/style.html',{'style':s_page,'paintings':paintings})

    def PaintStyDetail(request, s_slug, painting_slug):
        try:
            painting = Painting.objects.get(style_slug=s_slug, slug=painting_slug)
        except Exception as e:
          raise e
        return render(request, 'gallery/painting.html', {'painting':painting})

