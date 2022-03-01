from django.urls import path
from django.views.generic import TemplateView

from mainapp.views import MainSearch

app_name='mainapp'

urlpatterns = (
    path('home/', MainSearch, name='mainapp'),

)
