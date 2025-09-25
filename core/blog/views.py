from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Post, Category
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from .forms import PostForm
# Create your views here.


'''  TemplateView

class cbv(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Class Based View'
        context['posts'] = Post.objects.all()
        return context

'''

# Post List View
class postListView(ListView):

    model = Post
    template_name = 'post_list.html'
    context_object_name = 'articles'
    paginate_by = 2
    ordering = ['-created_at']

# Post Detail View
class postDetailView(DetailView):

    model = Post
    context_object_name = 'contact'

'''
# Add Post View 
class addPostView(FormView):
    template_name = 'blog/contact.html'
    form_class = PostForm
    success_url = '/blog/list/'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
''' 

# Create Post View
class CreatePostView(CreateView):

    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'
    success_url = '/blog/post/list/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
# Edit Post View
class editPostView(UpdateView):

    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'
    success_url = '/blog/post/list/'

class DeletePostView(DeleteView):

    model = Post
    template_name = 'blog/post_delete.html'
    success_url = '/blog/post/list/'
    
