from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

import postapp.models


def MainSearch(request) :
    return render(request, 'articleapp/list.html')


class PostListView(ListView):
    model = postapp.models.Post
    context_object_name = 'Post_list'
    template_name = 'postapp/list.html'
    paginate_by = 10