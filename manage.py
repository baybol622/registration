#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todolist.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # Проблемы с импортом Django, возможно, не установлен Django.
        try:
            import django
            raise ImportError(
                "Дjango не установлен. Пожалуйста, установите его с помощью `pip install django`."
            )
        except ImportError:
            raise

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
