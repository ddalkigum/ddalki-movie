from random import choice, randint
from django.core.management.base import BaseCommand
from django_seed import Seed
from reviews.models import Review
from users.models import User
from movies.models import Movie
from books.models import Book


class Command(BaseCommand):

    help = "This command seeds reviews"

    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            help="How many reviews do you want to create?",
            default=10)

    def handle(self, *args, **options):
        total = int(options.get('total'))
        seeder = Seed.seeder()
        users = User.objects.all()
        movies = Movie.objects.all()
        books = Book.objects.all()
        seeder.add_entity(
            Review, total, {
                "created_by": lambda x: choice(users),
                "text": lambda x: seeder.faker.sentence(),
                "movie": lambda x: choice(movies),
                "book": lambda x: choice(books),
                "rating": lambda x: randint(1, 5),
            })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'{total} reviews created!'))
