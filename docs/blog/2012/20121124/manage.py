#!/usr/bin/env python
import os
import sys
if __name__ == "__main__":
    os.environ[
        'DJANGO_SETTINGS_MODULE'] = 'lino_book.projects.20121124.settings'
    from lino.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
