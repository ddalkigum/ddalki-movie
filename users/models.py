from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse



class User(AbstractUser):

    PREF_BOOKS = "books"
    PREF_MOVIES = "movies"
    PREF_CHOICES = ((PREF_BOOKS, "Books"), (PREF_MOVIES, "Movies"))

    LANG_EN = "english"
    LANG_KR = "korean"
    LANG_CHOICES = (
      (LANG_EN, "English"),
      (LANG_KR, "Korean")
    )

    bio = models.TextField()
    preference = models.CharField(
        max_length=20, choices=PREF_CHOICES, default=PREF_MOVIES)
    language = models.CharField(
        max_length=20, choices=LANG_CHOICES, default=LANG_EN)
    fav_book_cat = models.ForeignKey("categories.Category", on_delete=models.SET_NULL, null=True, related_name="book_users")
    fav_movie_cat = models.ForeignKey("categories.Category", on_delete=models.SET_NULL, null=True, related_name="movie_users")

    def __str__(self):
      return self.username
    
    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})