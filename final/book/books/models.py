from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils.translation import ugettext_lazy as _

from six import python_2_unicode_compatible

from star_ratings.models import Rating


@python_2_unicode_compatible
class Tag(models.Model):
    """Tag model."""

    name = models.CharField(max_length=255)

    class Meta(object):
        """Options."""

        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Book(models.Model):
    """Book model."""

    title = models.CharField(max_length=255)
    image = models.ImageField(null=True,
                              blank=True,
                              upload_to='images')
    ratings = GenericRelation(Rating, related_query_name='books')
    prep_time = models.DurationField(null=True, blank=True)
    cooking_time = models.DurationField(null=True, blank=True)
    servings = models.CharField(null=True, blank=True, max_length=255)
    instructions = models.TextField()

    class Meta(object):
        """Options."""

        verbose_name = _("Book")
        verbose_name_plural = _("Books")

    def __str__(self):
        return self.title
