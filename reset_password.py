import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth.models import User

# Delete old admin and create new one
User.objects.filter(username='admin').delete()
user = User.objects.create_superuser('admin', 'usamaijaz404@gmail.com', 'usama1290')
print('✅ Admin password reset to: admin123')
print('You can now login with username: admin, password: usama1290')