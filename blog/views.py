from django.shortcuts import render, redirect, get_object_or_404
from .models import About, Author, Tag, SocialMedia, Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm


# Create your views here.


def home_view(request):
    posts = Post.objects.all().order_by('id')[:4]
    authors = Author.objects.all().order_by('id')[:1]
    social_media = SocialMedia.objects.all()
    context = {
        'posts': posts,
        'authors': authors,
        'social_media': social_media,
    }
    return render(request, 'index.html', context)


def articles_view(request):
    posts = Post.objects.all().order_by('-id')
    social_media = SocialMedia.objects.all()
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog.html', {'posts': posts, 'social_media': social_media})


def articles_view_detail(request, pk):
    form = CommentForm()
    social_media = SocialMedia.objects.all()
    post = get_object_or_404(Post, id=pk)
    tags = post.tags.all()
    tag = request.GET.get('tag')
    comments = Comment.objects.filter(post__id=pk).order_by('-id')
    if tag:
        tag = get_object_or_404(Tag, name=tag)
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            # comment = form.save(commit=False)
            # # comment.post = post
            # comment.save()
            form.save()
            return redirect(f'articles_view/{post.id}')
    else:
        form = CommentForm()
    context = {
        'form': form,
        'post': post,
        'tag': tag,
        'tags': tags,
        'comments': comments,
        'social_media': social_media
    }
    return render(request, 'blog-single.html', context)


def about_view(request):
    author = Author.objects.all().order_by('id')[:1]
    social_media = SocialMedia.objects.all()
    about = About.objects.all().order_by('id').first()
    context = {
        'authors': author,
        'about': about,
        'social_media': social_media
    }
    return render(request, 'about.html', context)
