from django.shortcuts import render
from movies.models import Movie
from books.models import Book
from people.models import Person
from categories.models import Category

def resolve_home(request):
  

  movies = Movie.objects.all().order_by('-pk')[:9]
  books = Book.objects.all().order_by('-pk')[:9]
  people = Person.objects.all().order_by('-pk')[:9]
  

  return render(request, "home.html", {
    "movies":movies,
    "books": books,
    "people": people,
    "page_title": "Home"
  })



def resolve_search(request):

  term = request.GET.get('term')

  movies = books = people = None

  if term:
    movies = Movie.objects.filter(title__startswith=term)
    books = Book.objects.filter(title__startswith=term)
    people = Person.objects.filter(name__startswith=term)

    print(movies, books, people)

  return render(request, "search.html", {
    "categories": Category.objects.all(),
    "movies":movies,
    "books": books,
    "term": term,
    "people": people
  })