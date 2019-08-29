from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Style, Painting
from .forms import SignUpForm
from django.contrib.auth.models import User, Group

def index(request):
    text_var = 'Ferguson Art Gallery Shop'
    return HttpResponse(text_var)    

def shopByStyle(request, s_slug=None):
    s_page = None
    paintings = None
    if s_slug!= None:
        s_page = get_object_or_404(Style,slug=s_slug)
        paintings = Painting.objects.filter(style=s_page,available=True)
    else: 
      paintings = Painting.objects.all().filter(available=True) 

    return render(request, 'gallery/style.html', {'style':s_page,'paintings':paintings})

def paintStyleDetail(request,s_slug,painting_slug):
    try:
        painting = Painting.objects.get(style__slug=s_slug,slug=painting_slug)
    
    except Exception as e:
      raise e
    return render(request, 'gallery/painting.html', {'painting':painting})

def signupTemp(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      user_signup = User.objects.get(username=username)
      customer_group_assign =  Group.objects.get(name='Customer')
      customer_group.user_set.add(user_signup)
  else:
    form = SignUpForm()
  return render(request, 'user_accounts/user_signup.html', {'form':form})