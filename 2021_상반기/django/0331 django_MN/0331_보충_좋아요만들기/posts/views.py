from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from django.http import HttpResponse, HttpResponseForbidden
from .models import Post, Comment
from .forms import PostForm, CommentForm


@require_safe
def index(request):
    posts = Post.objects.order_by('-pk')
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/create.html', context)


@require_safe
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment_form = CommentForm()
    comments = post.comment_set.all()
    context = {
        'post': post,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'posts/detail.html', context)


@require_POST
def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user.is_authenticated:
        if request.user == post.user:
            post.delete()
            return redirect('posts:index')
    return redirect('posts:detail', post.pk)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.user:
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('posts:detail', post.pk)
        else:
            form = PostForm(instance=post)
    else:
        return redirect('posts:index')
        # return HttpResponseForbidden()
    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'posts/update.html', context)
        

@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('posts:detail', post.pk)
        context = {
            'comment_form': comment_form,
            'post': post,
        }
        return render(request, 'posts/detail.html', context)
    return redirect('accounts:login')
    # return HttpResponse(status=401)


@require_POST
def comments_delete(request, post_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
        # return HttpResponseForbidden()
    return redirect('posts:detail', post_pk)
    # return HttpResponse(status=401)


@require_POST
def like(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.user in post.like_users.all():
    # 좋아요 누른 명단에 지금 내 아이디가 있다면
        post.like_users.remove(request.user)
    # 제거한다
    else:
        post.like_users.add(request.user)
    return redirect('posts:detail', post_pk)


