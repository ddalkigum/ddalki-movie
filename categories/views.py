from django.views.generic import DetailView
from categories.models import Category

class CategoryDetail(DetailView):
    model = Category
    context_object_name = 'category'