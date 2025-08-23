import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth.models import User

print("Creating admin user...")
User.objects.all().delete()  # Clear any existing
admin = User.objects.create_superuser('admin', 'admin@test.com', 'Pass123')
print('✅ SUCCESS! Admin created!')
print('Username: admin')
print('Password: Pass123')