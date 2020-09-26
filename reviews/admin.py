from django.contrib import admin
from reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

  list_display = ("created_by", "movie", "book", "rating")
  list_filter = ("movie", "book")