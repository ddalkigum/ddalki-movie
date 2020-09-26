from django.urls import path
from favs.views import resolve_add

app_name="favs"

urlpatterns = [
  path("toggle/<int:pk>", resolve_add, name="add"),
]
