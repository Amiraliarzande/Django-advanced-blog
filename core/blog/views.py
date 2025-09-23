from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Post, Category

# Create your views here.

def fbv(request):
    return render(request, 'home.html', context={'name' : 'Ferdows'})

class cbv(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Class Based View'
        context['posts'] = Post.objects.all()
        return context
        