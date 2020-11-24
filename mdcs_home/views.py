import logging

from django.conf import settings
from django.shortcuts import render
from django.urls import reverse

from core_main_app.access_control.exceptions import AccessControlError
from core_main_app.components.template_version_manager.api import (
    get_global_version_managers,
)

logger = logging.getLogger(__name__)


def template_list(request):
    """Display the last HOMEPAGE_NB_LAST_TEMPLATES templates.
    Args:
        request:

    Returns:

    """
    try:
        templates = [
            version_manager
            for version_manager in get_global_version_managers(request=request)
            if not version_manager.is_disabled
        ][: settings.HOMEPAGE_NB_LAST_TEMPLATES]
    except AccessControlError:
        templates = []
        logger.warning("Access Forbidden: unable to get template list.")
    context = {"templates": templates}
    return render(request, "mdcs_home/template_list.html", context)


def tiles(request):
    """

    :param request:
    :return:
    """
    from django.conf import settings

    installed_apps = settings.INSTALLED_APPS

    context = {"tiles": []}

    if "core_curate_app" in installed_apps:
        curate_tile = {
            "logo": "fa-edit",
            "link": reverse("core_curate_index"),
            "title": "Curate your Materials Data",
            "text": "Click here to select a form template and then fill out the corresponding form.",
        }

        context["tiles"].append(curate_tile)

    if "core_explore_example_app" in installed_apps:
        explore_example_tile = {
            "logo": "fa-flask",
            "link": reverse("core_explore_example_index"),
            "title": "Build your own queries",
            "text": "Click here to search for Materials Data in the repository using flexible queries.",
        }

        context["tiles"].append(explore_example_tile)

    if "core_explore_keyword_app" in installed_apps:
        explore_keywords_tile = {
            "logo": "fa-search",
            "link": reverse("core_explore_keyword_app_search"),
            "title": "Search by keyword",
            "text": "Click here to explore for Materials Data in the repository using keywords.",
        }

        context["tiles"].append(explore_keywords_tile)

    if "core_composer_app" in installed_apps:
        compose_tile = {
            "logo": "fa-file-code",
            "link": reverse("core_composer_index"),
            "title": "Compose a template",
            "text": "Click here to compose your own template.",
        }

        context["tiles"].append(compose_tile)

    return render(request, "mdcs_home/tiles.html", context)
