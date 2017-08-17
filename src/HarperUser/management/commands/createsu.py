from django.core.management.base import BaseCommand
from HarperUser.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="admin").exists():
            user = User.objects.create(
                username="admin",
                email="Zacharybedrosian@gmail.com",
                first_name="Zachary",
                last_name="Bedrosian",
                is_staff=True,
                is_superuser=True,

            )
            user.set_password("Bedrock123")
            user.save()
