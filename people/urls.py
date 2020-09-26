from django.urls import path
from people.views import PeopleView, PersonDetail, CreatePerson, UpdatePerson

app_name="people"

urlpatterns = [
  path("", PeopleView.as_view(), name="people"),
  path("<int:pk>", PersonDetail.as_view(), name="person"),
  path("<int:pk>/update", UpdatePerson.as_view(), name="update"),
  path("create", CreatePerson.as_view(), name="create"),
]
