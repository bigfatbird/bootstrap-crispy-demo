from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.http import HttpResponse
from django.shortcuts import render
from .forms import *


# Create your views here.
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_blog_posts'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

def BlogCreateView(request):
    context = {}

    if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = MessageForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                form.save()
            context['form']= form
            return render(request, 'post_new.html', context)
    else:
        form = MessageForm()
    return render(request, 'post_new.html', {'form': form})



    # return render(request, 'name.html', {'form': form})


    # model = Post
    # template_name = 'post_new.html'
    # fields = ['title', 'email_field', 'author', 'body']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
