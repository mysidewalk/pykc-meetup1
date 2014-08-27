#!/usr/bin/env python

if __name__ == "__main__":
    import os
    import sys

    BASE_DIR = os.path.dirname(__file__)
    sys.path.insert(0, BASE_DIR)

    # set environment from environment var ENVIRONMENT
    environment = os.getenv('ENVIRONMENT', 'development')
    os.putenv('ENVIRONMENT', environment)
    # redundant but apparently necessary
    os.environ['ENVIRONMENT'] = environment

    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.' + environment

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
