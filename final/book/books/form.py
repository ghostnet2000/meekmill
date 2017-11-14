from django import forms
from django.forms import modelformset_factory, formset_factory

from djangoformsetjs.utils import formset_js_path

from .models import Book


class BookForm(forms.ModelForm):
    """Book form."""

    class Meta(object):
        """Options."""

        model = Book
        fields = (
            'id',
            'title',
            'image',
            'prep_time',
            'cooking_time',
            'servings',
            'instructions',
        )
