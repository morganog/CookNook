from django.shortcuts import render,redirect
from .models import Post,Upload


def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'cooknookapp/home.html', context)

def about(request):
    return render(request, 'cooknookapp/about.html', {'title': 'About'})

def account(request):
    return render(request, 'cooknookapp/account.html')
def upload(request):
    if request.method == 'POST':
        data = request.POST
        files = request.FILES
        n = data.get('name')
        d = data.get('descp')
        i = files.get('image')
        v=files.get('video')
        Upload.objects.create(name=n, descp=d, image=i)
        return redirect('/')
    queryset = Post.objects.all()
    context = {'receipies': queryset}
    return render(request, 'cooknookapp/upload.html', context)
