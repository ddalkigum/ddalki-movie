from random import choice
from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User
from categories.models import Category

class Command(BaseCommand):

    help = "This command seeds users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--total", help="How many users do you want to create?", default=10)

    def handle(self, *args, **options):
        total = int(options.get('total'))
        seeder = Seed.seeder()
        movies = Category.objects.filter(kind=Category.KIND_MOVIE)
        books = Category.objects.filter(kind=Category.KIND_BOOK)
        seeder.add_entity(User, total, {
            "is_staff": False,
            "is_superuser": False,
            "preference": lambda x: choice([User.PREF_BOOKS, User.PREF_MOVIES]),
            "fav_book_cat": lambda x: choice(books),
            "fav_movie_cat": lambda x: choice(movies)
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'{total} users created!'))
