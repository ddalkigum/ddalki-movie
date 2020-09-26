from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User


@admin.register(User)
class UserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + ((
        "Custom Profile",
        {
            "fields": (
                "bio",
                "preference",
                "language",
                "fav_book_cat",
                "fav_movie_cat",
            )
        },
    ), )

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "preference",
        "language",
        "fav_book_cat",
        "fav_movie_cat",
    )

    list_filter = (
        "preference",
        "language",
        "fav_book_cat",
        "fav_movie_cat",
    )
