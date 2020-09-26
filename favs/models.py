from django.db import models
from core.models import CoreModel

class FavList(CoreModel):
  
  """ Favourite List """

  created_by = models.OneToOneField("users.User", on_delete=models.CASCADE)
  books = models.ManyToManyField("books.Book", related_name="fav_lists")
  movies = models.ManyToManyField("movies.Movie", related_name="fav_lists")

  def __str__(self):
    return f"{self.created_by}'s Fav List'"