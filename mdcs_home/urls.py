"""mdcs URL Configuration
"""

from django.urls import re_path

from mdcs_home import views

urlpatterns = [
    re_path(r"^tiles", views.tiles, name="mdcs_home_tiles"),
    re_path(r"^templates", views.template_list, name="mdcs_home_templates"),
]
