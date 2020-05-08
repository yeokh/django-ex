#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
    
    from django.core.management import execute_from_command_line

    print("REDHAT Demo Log Message")
    sys.stderr.write("REDHAT DEMO Error Message\n")
    
    execute_from_command_line(sys.argv)
