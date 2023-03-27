""" Admin urls
"""

from core_main_app.utils.admin_site.model_admin_class import (
    register_simple_history_models,
)
from django.conf import settings

DJANGO_SIMPLE_HISTORY_MODELS = getattr(
    settings, "DJANGO_SIMPLE_HISTORY_MODELS", None
)
register_simple_history_models(DJANGO_SIMPLE_HISTORY_MODELS)
