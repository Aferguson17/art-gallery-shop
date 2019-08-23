from django.shortcuts import render
from gallery.models import Painting
from django.db.models import Q

def searchResults(request):
    paintings = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        paintings = Painting.objects.all().filter(Q(title__contains=query) | Q(description__contains=query))
    return render(request, 'search.html', {'query':query, 'paintings':paintings})