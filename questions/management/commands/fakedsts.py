
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from questions.model import Question
from django.db import transaction

from faker import Faker
fake = Faker()

class Command(BaseCommand):
    
    def ass_arguments(self, parser):
        parser.add_argument('--users', type=int,default=0)
        parser.add_argument('--questions', type=int,default=0)

    def handle(self, *args, **options):
        with transaction.atomic():
            for _ in range(options.get('users')):
                try:
                    User.objects.create_user(fake.user_name())
                except IntegrityError:
                    pass
        uids = list(User.objects.values_list('pk', flat=True))
        with transacrion.atomic():
            for _ in range(options.get('questions')):
                try:
                    Users.objects.create_user(fake.)

