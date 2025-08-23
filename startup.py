import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth.models import User

# Delete all users and create fresh admin
User.objects.all().delete()
admin = User.objects.create_superuser('admin', 'admin@test.com', 'Pass123')
print('✅ ADMIN CREATED!')
print('Username: admin')
print('Password: Pass123')