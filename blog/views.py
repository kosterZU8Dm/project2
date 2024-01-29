from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def main_page(request):
    posts = Post.objects.order_by('-created_at')  # Сортировка по дате добавления
    return render(request, 'blog/main_page.html', {'posts': posts})

def search(request):
    query = request.GET.get('q', '')
    posts = Post.objects.filter(title__icontains=query)
    return render(request, 'blog/main_page.html', {'posts': posts, 'query': query})

def contacts(request):
    return render(request, 'blog/contacts.html')