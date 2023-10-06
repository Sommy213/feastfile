from django.shortcuts import render,redirect
from django.contrib.auth import  login
from .forms import RegistrationForm
from .forms import BlogForm
from .models import WeEat


def landding(request):
    return render(request,'index.html')

def home(request):
    home_page = WeEat.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'home_page':home_page})

def create_blog(request):

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES) 
        if form.is_valid():
            blog = form.save(commit=False)

            blog.save()
            return redirect('feastfiles:home')
    else:
        form = BlogForm()
    
    return render(request, 'post.html', {'form': form})


def My_blog(request):
    return render(request, 'create_blog.html')
def wait_please(request):
    return render(request, 'wait.html')

def register(request):
    form = RegistrationForm
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post.html')
        print(form.errors)
    return render(request, 'signup.html', {'form': form})
 







