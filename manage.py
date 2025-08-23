#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# ADD THIS BLOCK
if 'runserver' not in sys.argv and 'migrate' in sys.argv:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    import django
    django.setup()
    from django.contrib.auth.models import User
    if User.objects.count() == 0:
        User.objects.create_superuser('admin', 'admin@test.com', 'Pass123')
        print('✅ ADMIN CREATED! Username: admin, Password: Pass123')
# END OF BLOCK


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
