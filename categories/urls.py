from django.urls import path
from categories.views import CategoryDetail

app_name="categories"

urlpatterns = [
  path("<int:pk>", CategoryDetail.as_view(), name="category"),
]
