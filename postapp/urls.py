from django.urls import path
from django.views.generic import TemplateView

from postapp.views import PostCreateView, PostDeleteView, PostDetailView, PostListView

app_name = 'postapp'

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='create'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>', PostDetailView.as_view(), name='detail'),
    path('list/', PostListView.as_view(), name='list'),
]



