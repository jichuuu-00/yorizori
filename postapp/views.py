from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy
from postapp.forms import PostCreationForm
from postapp.models import Post


class PostCreateView(CreateView):
    model = Post
    form_class = PostCreationForm
    template_name = 'postapp/create.html'

    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.save()
        return super().form_valid(form)