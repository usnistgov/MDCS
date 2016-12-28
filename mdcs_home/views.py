from django.core.urlresolvers import reverse
from django.shortcuts import render
from core_main_app.components.template_version_manager.api import get_global_version_managers


def template_list(request):
    """

    :param request:
    :return:
    """
    context = {
        "templates": [version_manager for version_manager in get_global_version_managers()
                      if not version_manager.is_disabled]
    }

    return render(request, "mdcs_home/template_list.html", context)


def tiles(request):
    """

    :param request:
    :return:
    """
    from django.conf import settings
    installed_apps = settings.INSTALLED_APPS

    # TODO Remove the next lines once curate, explore and compose are online
    installed_apps = list(installed_apps)
    installed_apps.append("core_explore_app")
    installed_apps.append("core_compose_app")

    context = {
        "tiles": []
    }

    if "core_curate_app" in installed_apps:
        curate_tile = {
            "logo": "fa-edit",
            "link": reverse("core_curate_index"),
            "title": "Curate your Materials Data",
            "text": "Click here to select a form template and then fill out the corresponding form."
        }

        context["tiles"].append(curate_tile)

    if "core_explore_app" in installed_apps:
        explore_tile = {
            "logo": "fa-search",
            "link": reverse("core_website_homepage"),  # FIXME Change it the correct URL
            "title": "Explore the repository",
            "text": "Click here to search for Materials Data in the repository using flexible queries."
        }

        context["tiles"].append(explore_tile)

    if "core_compose_app" in installed_apps:
        compose_tile = {
            "logo": "fa-file-code-o",
            "link": reverse("core_website_homepage"),  # FIXME Change it the correct URL
            "title": "Compose a template",
            "text": "Click here to compose your own template."
        }

        context["tiles"].append(compose_tile)

    return render(request, "mdcs_home/tiles.html", context)
