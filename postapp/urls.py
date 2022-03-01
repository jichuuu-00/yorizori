from django.urls import path
from django.views.generic import TemplateView

from postapp.views import PostCreateView, PostDeleteView

app_name = 'postapp'

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='create'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete'),
]



