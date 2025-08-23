def create_superuser():
    from django.contrib.auth import get_user_model
    User = get_user_model()

    if not User.objects.filter(username='boss').exists():
        User.objects.create_superuser('boss', 'boss@test.com', 'boss123')
        print('Boss user created!')
    else:
        # Reset password for existing user
        user = User.objects.get(username='boss')
        user.set_password('boss123')
        user.save()
        print('Boss password reset!')