from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path("movies/", include("movies.urls", namespace="movies")),
    path("books/", include("books.urls", namespace="books")),
    path("categories/", include("categories.urls", namespace="genres")),
    path("people/", include("people.urls", namespace="people")),
    path("users/", include("users.urls", namespace="users")),
    path("favs/", include("favs.urls", namespace="favs")),
    path("admin/", admin.site.urls),
    path("sentry-debug/", trigger_error),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    