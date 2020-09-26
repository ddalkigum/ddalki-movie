from django import forms
from . import models


class ReviewForm(forms.ModelForm):
    class Meta:

        model = models.Review

        fields = (
            "created_by",
            "text",
            "movie",
            "book",
            "rating",
        )