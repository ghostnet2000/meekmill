from django.contrib import admin

from .models import Book

class BookAdmin(admin.ModelAdmin):
    """Book admin."""

    fields = (
        'title',
        'image',
        'prep_time',
        'cooking_time',
        'servings',
        'instructions',
    )

# Register your models here.
admin.site.register(Book, BookAdmin)
