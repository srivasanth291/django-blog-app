from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost
from .forms import BlogPostForm
from django.db.models import Q
from django.core.paginator import Paginator

def post_list(request):
    query = request.GET.get('q')

    if query:
        posts = BlogPost.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).order_by('-created_at')
    else:
        posts = BlogPost.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 5) 
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'query': query
    })

def post_detail(request, id):
    post = get_object_or_404(BlogPost, id=id)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = BlogPostForm()
    return render(request, 'blog/post_form.html', {'form': form})

def post_update(request, id):
    post = get_object_or_404(BlogPost, id=id)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', id=post.id)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})

def post_delete(request, id):
    post = get_object_or_404(BlogPost, id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})
