"""mdcs URL Configuration
"""
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^tiles', views.tiles, name=""),
    url(r'^templates', views.template_list, name=""),
]

