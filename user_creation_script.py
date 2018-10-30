from django.contrib.auth.models import User
if User.objects.filter(username='admin').count() == 0:
    User.objects.create_superuser('admin', 'admin@example.com', 'pass')

