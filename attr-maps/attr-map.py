""" SAML attribute mapping
"""
from core_main_app.utils.saml2.utils import load_attribute_map_from_env

MAP = load_attribute_map_from_env()
