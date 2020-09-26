from django.core.management.base import BaseCommand
from categories.models import Category

class Command(BaseCommand):

    help = "This command seeds categories"

    both_genres = [
        "Adventure",
        "Fantasy",
        "History",
        "Horror",
        "Mystery",
        "Romance",
        "Thriller",
    ]
    movie_genres = [
        "Action", "Animation", "Biography", "Comedy", "Crime",
        "Documentary", "Drama", "Family",  "Film Noir", 
         "Music", "Musical", "Sci-Fi",
        "Short Film", "Sport", "Superhero", "War", "Western"
    ]
    book_genres = [
        "Contemporary",
        "Dystopian",
        "Paranormal",
        "Historical fiction",
        "Science Fiction",
        "Memoir",
        "Cooking",
        "Art",
        "Self-help / Personal",
        "Development",
        "Motivational",
        "Health",
        "Travel",
        "Guide / How-to",
        "Families & Relationships",
        "Humor",
        "Children’s",
    ]

    def handle(self, *args, **options):
        for genre in self.both_genres:
          Category.objects.get_or_create(
            name=genre,
            kind=Category.KIND_BOTH
          )
        for genre in self.movie_genres:
          Category.objects.get_or_create(
            name=genre,
            kind=Category.KIND_MOVIE
          )
        for genre in self.book_genres:
          Category.objects.get_or_create(
            name=genre,
            kind=Category.KIND_BOOK
          )
        self.stdout.write(self.style.SUCCESS('Categories created!'))
