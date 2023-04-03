from django.shortcuts import render, get_object_or_404

from .models import Group, Post

POSTS_PER_PAGE = 10


def index(request):
    posts = (
        Post.objects.select_related('author', 'group')
        [:POSTS_PER_PAGE]
    )

    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_list(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:POSTS_PER_PAGE]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
