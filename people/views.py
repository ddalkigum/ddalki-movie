from django.views.generic import ListView, DetailView, CreateView, UpdateView
from people.models import Person


class PeopleView(ListView):
  
  model = Person
  paginate_by = 15
  paginate_orphans = 5
  ordering = "-created_at"
  context_object_name = "people"
  template_name = "people/people_list.html"

  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "All People"
        return context


class PersonDetail(DetailView):
  model = Person
  template_name = "people/person_detail.html"
  context_object_name = 'person'


class CreatePerson(CreateView):
  model = Person
  fields = (
    "name",
    "photo",
    "kind",  
  )

class UpdatePerson(UpdateView):
  model = Person
  fields = (
    "name",
    "photo",
    "kind"
  )