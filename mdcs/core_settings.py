""" Django settings for core applications.
"""
import os

SERVER_URI = os.environ["SERVER_URI"] if "SERVER_URI" in os.environ else None

# Website customization
WEBSITE_SHORT_TITLE = "MDCS"
CUSTOM_DATA = "Materials Data"
CUSTOM_NAME = os.environ["SERVER_NAME"] if "SERVER_NAME" in os.environ else "Curator"
CUSTOM_TITLE = "Materials Data Curation System"
CUSTOM_SUBTITLE = "Part of the Materials Genome Initiative"
CURATE_MENU_NAME = "Data Curation"
WEBSITE_ADMIN_COLOR = "yellow"
# black, black-light, blue, blue-light, green, green-light, purple, purple-light, red, red-light, yellow, yellow-light

DATA_SOURCES_EXPLORE_APPS = [
    "core_explore_federated_search_app",
    "core_explore_oaipmh_app",
]

# Lists in data not stored if number of elements is over the limit (e.g. 100)
SEARCHABLE_DATA_OCCURRENCES_LIMIT = None

PARSER_DOWNLOAD_DEPENDENCIES = True
""" boolean: Does the parser download dependencies
"""

EXPLORE_ADD_DEFAULT_LOCAL_DATA_SOURCE_TO_QUERY = True
""" boolean: Do we add the local data source to new queries by default
"""

SSL_CERTIFICATES_DIR = True
""" Either a boolean, in which case it controls whether requests verify the server's TLS certificate, 
or a string, in which case it must be a path to a CA bundle to use.
"""

XSD_URI_RESOLVER = "REQUESTS_RESOLVER"
""" :py:class:`str`: XSD URI Resolver for lxml validation. Choose from:  None, 'REQUESTS_RESOLVER'.
"""

DISPLAY_EDIT_BUTTON = True
""" boolean: Display the edit button on the result page
"""
DATA_SORTING_FIELDS = ["-last_modification_date"]
""" Array<string>: Default sort fields for the data query. 
"""
DATA_DISPLAYED_SORTING_FIELDS = [
    {
        "field": "last_modification_date",
        "display": "Last updated",
        "ordering": "-last_modification_date",
    },
    {
        "field": "last_modification_date",
        "display": "First updated",
        "ordering": "+last_modification_date",
    },
    {"field": "title", "display": "Titles (A-Z)", "ordering": "+title"},
    {"field": "title", "display": "Titles (Z-A)", "ordering": "-title"},
    {"field": "template", "display": "Templates", "ordering": "+template"},
]
"""The default sorting fields displayed on the GUI, Data model field Array"""
SORTING_DISPLAY_TYPE = "single"
"""Result sorting graphical display type ('multi' / 'single')"""
DEFAULT_DATE_TOGGLE_VALUE = True
""" boolean: Set the toggle default value in the records list
"""
DISPLAY_PRIVACY_POLICY_FOOTER = False
""" boolean: display the privacy policy link in the footer
"""
DISPLAY_TERMS_OF_USE_FOOTER = True
""" boolean: display the terms of use link in the footer
"""
DISPLAY_CONTACT_FOOTER = False
""" boolean: display the contact link in the footer
"""
DISPLAY_HELP_FOOTER = False
""" boolean: display the help link in the footer
"""
DISPLAY_RULES_OF_BEHAVIOR_FOOTER = False
""" boolean: display the rules of behavior link in the footer
"""

ID_PROVIDER_SYSTEMS = {
    "local": {
        "class": "core_linked_records_app.utils.providers.local.LocalIdProvider",
        "args": [],
    },
    # "handle": {
    #     "class": "core_linked_records_app.utils.providers.handle_net.HandleNetSystem",
    #     "args": [
    #         "https://handle-server.example.org:8000",
    #         "300%3APREFIX/USER",
    #         "password",
    #     ],
    # },
}
""" dict: provider systems available for registering PIDs.
"""

ID_PROVIDER_PREFIXES = ["cdcs"]
""" list<str>: accepted providers if manually specifying PIDs (first item is the
default prefix)
"""

PID_XPATH = "root.pid"
""" string: location of the PID in the document, specified as dot notation
"""

AUTO_SET_PID = False
""" boolean: enable the automatic pid generation for saved data.
"""
