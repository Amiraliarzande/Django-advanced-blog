from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Post, Category
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

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

# ListView
class postListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'articles'
    paginate_by = 2
    ordering = ['-created_at']


class postDetailView(DetailView):
    model = Post
    context_object_name = 'contact'
    
