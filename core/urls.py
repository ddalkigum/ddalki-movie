from django.urls import path
from core.views import resolve_home, resolve_search

app_name="core"

urlpatterns = [
  path("", resolve_home, name="home"),
  path("search", resolve_search, name="search")
]
