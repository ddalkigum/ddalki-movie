from django.shortcuts import render, redirect, reverse
from favs.models import FavList
from movies.models import Movie
from books.models import Book

def resolve_add(request, pk):

  kind = request.GET.get('kind', 'movie')
  
  user = request.user

  if user.is_authenticated:

    fav_list, _ = FavList.objects.get_or_create(created_by=user)

    if kind == 'movie':
      movie = Movie.objects.get(pk=pk)
      if movie in fav_list.movies.all():
        fav_list.movies.remove(movie)
      else:
        fav_list.movies.add(movie)
      fav_list.save()
      return redirect(reverse('movies:movie', kwargs={'pk': pk}))
    else:
      book = Book.objects.get(pk=pk)
      if book in fav_list.books.all():
        fav_list.books.remove(book)
      else:
        fav_list.books.add(book)
      fav_list.save()
      return redirect(reverse('books:book', kwargs={'pk': pk}))