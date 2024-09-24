from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'cooknookapp/home.html', context)

def about(request):
    return render(request, 'cooknookapp/about.html', {'title': 'About'})

def account(request):
    return render(request, 'cooknookapp/account.html')
