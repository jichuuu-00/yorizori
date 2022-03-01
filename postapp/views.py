import json

from django.http import request
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import FormMixin

from postapp.forms import PostCreationForm, CommentCreationForm
from postapp.models import Post


class PostCreateView(CreateView):
    model = Post
    form_class = PostCreationForm
    template_name = 'postapp/create.html'

    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.recipe_type = self.request.POST.getlist('food[]')
        temp_article.recipe_material = self.request.POST.getlist('Ingredients[]')
        temp_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('postapp:detail', kwargs={'pk': self.object.pk})



class PostDeleteView(DeleteView):
    model = Post
    context_object_name = 'target_article'
    success_url = reverse_lazy('postapp:list')
    template_name = 'postapp/delete.html'


class PostDetailView(DetailView, FormMixin):
    model = Post
    form_class = PostCreationForm
    context_object_name = 'target_post'
    template_name = 'postapp/detail.html'

class PostListView(ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'postapp/list.html'
    paginate_by = 10