from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@admin.admin',
            first_name='Admin',
            last_name='Admin',
            is_active=True,
            is_staff=True,
            is_superuser=True
        )
        user.set_password('1234qwer')
        user.save()
