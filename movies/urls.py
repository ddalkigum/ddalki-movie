from django.urls import path
from movies.views import (
    MoviesView,
    MovieDetail,
    CreateMovie,
    UpdateMovie,
    MoiveReviewView,
)

app_name = "movies"

urlpatterns = [
    path("", MoviesView.as_view(), name="movies"),
    path("<int:pk>", MovieDetail.as_view(), name="movie"),
    path("<int:pk>/review/", MoiveReviewView.as_view(), name="review"),
    path("<int:pk>/update", UpdateMovie.as_view(), name="update"),
    path("create", CreateMovie.as_view(), name="create"),
]
