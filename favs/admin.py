from django.contrib import admin
from favs.models import FavList

@admin.register(FavList)
class FavListAdmin(admin.ModelAdmin):

  list_display = ("created_by",)
