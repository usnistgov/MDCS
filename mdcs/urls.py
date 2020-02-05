"""mdcs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  re_path(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  re_path(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  re_path(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import re_path

from core_parser_app.tools.modules.discover import discover_modules

urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    re_path(r"^admin/defender/", include("defender.urls")),
    re_path(r"^o/", include("oauth2_provider.urls", namespace="oauth2_provider")),
    re_path(r"^", include("core_main_app.urls")),
    re_path(r"^home/", include("mdcs_home.urls")),
    re_path(r"^", include("core_website_app.urls")),
    re_path(r"^curate/", include("core_curate_app.urls")),
    re_path(r"^composer/", include("core_composer_app.urls")),
    re_path(r"^parser/", include("core_parser_app.urls")),
    re_path(r"^exporter/", include("core_exporters_app.urls")),
    re_path(r"^explore/common/", include("core_explore_common_app.urls")),
    re_path(r"^explore/example/", include("core_explore_example_app.urls")),
    re_path(
        r"^explore/federated/search/", include("core_explore_federated_search_app.urls")
    ),
    re_path(r"^federated/search/", include("core_federated_search_app.urls")),
    re_path(r"^explore/keyword/", include("core_explore_keyword_app.urls")),
    re_path(r"^oaipmh_search/", include("core_explore_oaipmh_app.urls")),
    re_path(r"^dashboard/", include("core_dashboard_app.urls")),
    re_path(r"^oai_pmh/", include("core_oaipmh_harvester_app.urls")),
    re_path(r"^oai_pmh/server/", include("core_oaipmh_provider_app.urls")),
    re_path(r"^file-preview/", include("core_file_preview_app.urls")),
    re_path(r"^", include("core_module_blob_host_app.urls")),
    re_path(r"^", include("core_module_remote_blob_host_app.urls")),
    re_path(r"^", include("core_module_advanced_blob_host_app.urls")),
    re_path(r"^", include("core_module_excel_uploader_app.urls")),
    re_path(r"^", include("core_module_periodic_table_app.urls")),
    re_path(r"^", include("core_module_chemical_composition_simple_app.urls")),
    re_path(r"^", include("core_module_chemical_composition_app.urls")),
    re_path(r"^", include("core_module_text_area_app.urls")),
    re_path(r"^pid/", include("core_linked_records_app.urls")),
]

# TODO: see if we can automate the discovery and run it from parser app
discover_modules(urlpatterns)
