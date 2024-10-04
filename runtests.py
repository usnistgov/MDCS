#!/usr/bin/env python
""" Run tests
"""
import os
import sys

import django
from django.conf import settings
from django.core.management import execute_from_command_line
from django.test.utils import get_runner

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.test_settings")
    execute_from_command_line(["", "migrate"])
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(["tests"])
    sys.exit(bool(failures))
