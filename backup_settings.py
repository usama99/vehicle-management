# Backup settings for direct database access
import os

DATABASE_URL = os.environ.get('DATABASE_URL', '')
if DATABASE_URL:
    print(f"Database URL found: {DATABASE_URL[:30]}...")
else:
    print("WARNING: No database URL found!")