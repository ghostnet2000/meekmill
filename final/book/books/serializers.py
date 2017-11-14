from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.HyperlinkedModelSerializer):
    """Book serializer."""

    image = serializers.ImageField(max_length=None,use_url=True)

    class Meta(object):
        """Options."""

        model = Book
        fields = (
            'id',
            'title',
            'author',
            'description',
            'year',
            'image',
        )

    def create(self, validated_data):
        """Create."""
        # Create Book without tags
        tags_data = validated_data.pop('title')
        book = models.Book.objects.create(**validated_data)

        return book

    def update(self, instance, validated_data):
        
        instance.title = validated_data.get('title')
        instance.author = validated_data.get('author')
        instance.description = validated_data.get('description')
        instance.year = validated_data.get('year')
        instance.image = validated_data.get('image')

        instance.save()

        return instance
