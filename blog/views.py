from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, PostForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

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

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('main_page')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user == post.author or request.user.userprofile.is_special_user:
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('main_page')
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/edit_post.html', {'form': form, 'post': post})
    else:
        return HttpResponseForbidden("You don't have permission to edit this post.")