from django.contrib import admin

from .models import Book

class BookAdmin(admin.ModelAdmin):
    """Book admin."""

	fields = (
	    'id',
	    'title',
	    'author',
	    'description',
	    'year',
	    'image',
	)

# Register your models here.
admin.site.register(Book, BookAdmin)
