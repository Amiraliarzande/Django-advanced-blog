from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Post, Category
from django.views.generic.list import ListView

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

class postListView(ListView):
    
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(status=True)
