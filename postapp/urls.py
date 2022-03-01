from django.urls import path
from django.views.generic import TemplateView

from postapp.views import PostCreateView

app_name = 'postleapp'

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='create'),
]



