from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import SignUpForm

def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/posts_list.html', {'posts': posts})

def main_page(request):
    posts = Post.objects.order_by('-created_at')  # сортировка по дате добавления
    return render(request, 'blog/main_page.html', {'posts': posts})

def search(request):
    query = request.GET.get('q', '')
    posts = Post.objects.filter(title__icontains=query)
    return render(request, 'blog/main_page.html', {'posts': posts, 'query': query})

def contacts(request):
    return render(request, 'blog/contacts.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('main_page')
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main_page')
    else:
        login_form = AuthenticationForm()
    return render(request, 'blog/login.html', {'login_form': login_form})