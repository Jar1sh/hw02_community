from django.shortcuts import render, get_object_or_404

from .models import Group, Post

QUANTITY_POSTS = 10


def index(request):
    posts = (
        Post.objects.all().select_related('author', 'group')
        [:QUANTITY_POSTS]
    )

    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_list(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:QUANTITY_POSTS]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
