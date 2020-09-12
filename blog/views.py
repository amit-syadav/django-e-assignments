from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Post,Assignment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from random import shuffle


def home(request):
	context = {
		'posts':Post.objects.all()
	}
	return render(request, 'blog/home.html',context)

class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'	# <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 5

@login_required
def ur_assign_view(request):
	
	if Assignment.objects.filter(assigned_to = request.user).count()!=5:
		rndm = list(Post.objects.all().exclude(author = request.user))
		shuffle(rndm)
		post = rndm[0:5]
		for x in post:
			# a = Assignment(quest = x.content, q_author = request.user)
			a = Assignment( post = x ,assigned_to = request.user)
			a.save()
	# else:
	print(" Assignmetn Already exists")
	post = Assignment.objects.filter(assigned_to = request.user)
	print(post,"\n\n\n")
	assgn = {
		'psts' : post
		}
	return render(request, 'blog/getassign.html', assgn)

# @login_required
# def gen_assign(request):
	
# 	post = Assignment.objects.all()
# 	assgn = {
# 		'psts' : post
# 		}
# 	return render(request, 'blog/genassign.html', assgn)

class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_posts.html'	# <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
	model = Post
	

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


def about(request):
	return render(request, 'blog/about.html')
