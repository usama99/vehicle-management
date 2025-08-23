import os
import sys
import django

print("="*50)
print("NUCLEAR RESET STARTING...")
print("="*50)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth.models import User
from django.db import connection

# Clear EVERYTHING
print("1. Deleting ALL users...")
User.objects.all().delete()
print(f"   Users remaining: {User.objects.count()}")

# Create fresh admin
print("2. Creating fresh admin...")
admin = User.objects.create_superuser(
    username='boss',
    email='usamaijaz404@gmail.com',
    password='boss123'
)
admin.save()
print(f"   Admin created: {admin.username}")

# Verify
print("3. Verifying...")
all_users = User.objects.all()
print(f"   Total users: {all_users.count()}")
for u in all_users:
    print(f"   - Username: {u.username}, Is Admin: {u.is_superuser}")

print("="*50)
print("RESET COMPLETE!")
print("LOGIN CREDENTIALS:")
print("Username: boss")
print("Password: boss123")
print("="*50)

# Force exit to ensure script completes
sys.exit(0)