"""mdcs URL Configuration
"""
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^tiles', views.tiles, name="mdcs_home_tiles"),
    url(r'^templates', views.template_list, name="mdcs_home_templates"),
]

