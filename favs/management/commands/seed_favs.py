from django.core.management.base import BaseCommand
from favs.models import FavList
from users.models import User
from movies.models import Movie
from books.models import Book


class Command(BaseCommand):

    help = "This command seeds lists"

    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            help="How many lists do you want to create?",
            default=10)

    def handle(self, *args, **options):
        total = int(options.get('total'))
        users = User.objects.all()[:total]
        movies = Movie.objects.all()
        books = Book.objects.all()
        for user in users:
          fav_list = FavList.objects.create(
            created_by=user,
          )
          fav_list.movies.set(choices(movies))
          fav_list.books.set(choices(books))
        self.stdout.write(self.style.SUCCESS(f'{total} lists created!'))
