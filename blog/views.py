from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from .models import Post, Comment, PostImage
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from .forms import PostForm, CommentForm,PostImageForm, PostImageFormSet
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect


def home(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/home.html', {'posts':posts})
def post_list(request):
	posts = Post.objects.filter(none_date__isnull=False)
	posts = Post.objects.filter(delete_date__isnull=True)

	return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request,pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post':post})
def signup(request):
    """signup
    to register users
    """
    if request.method == "POST":
        userform = UserCreationForm(request.POST)
        if userform.is_valid():
            userform.save()

            return render(request, 'blog/post_list.html')
    elif request.method == "GET":
        userform = UserCreationForm()

    return render(request, "registration/signup.html", {"userform": userform})
def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response

@login_required
def post_new(request):

	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			postimage_formset = PostImageFormSet(request.POST, request.FILES, instance=post)
			if postimage_formset.is_valid():
				post.author = request.user
				post.created_date = timezone.now()
				post.none_date=timezone.now()
				post.save()

				postimage_formset.save()
				return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
		postimage_formset = PostImageFormSet()
	return render(request, 'blog/add_picture_to_post.html', {'form': form, 'postimage_formset': postimage_formset})
@login_required
def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST,instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			postimage_formset = PostImageFormSet(request.POST, request.FILES, instance=post)
			if postimage_formset.is_valid():
				post.author = request.user
				post.published_date = timezone.now()
				post.save()
				postimage_formset.save()
				return redirect('blog.views.post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
		postimage_formset = PostImageFormSet(instance=post)
	return render(request, 'blog/add_picture_to_post.html', {'form': form, 'postimage_formset': postimage_formset})

@login_required
def post_remove(request, pk):
	post = get_object_or_404(Post,pk=pk)
	post.delete_date = timezone.now()
	post.save()
	return redirect('blog.views.post_list')
@login_required
def post_realremove(request, pk):
	post = get_object_or_404(Post,pk=pk)
	post.delete()

	return redirect('blog.views.post_list')
	#return redirect('blog.views.post_detail', pk=post_pk)
def post_draft_list(request):
	posts = Post.objects.filter(delete_date__isnull=False)
	return render(request, 'blog/post_draft_list.html', {'posts': posts})
def post_publish(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.publish()
	return redirect('blog.views.post_detail',pk=pk)
def publish(self):
	self.published_date = timezone.now()
	self.save()


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})
@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blog.views.post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog.views.post_detail', pk=post_pk)

def popup(request):
	return render(request,'blog/popup.html')
