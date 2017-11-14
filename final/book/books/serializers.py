from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    """Book serializer."""

    image = serializers.ImageField(max_length=None,use_url=True)

    class Meta(object):
        """Options."""

        model = Book
        fields = (
            'id',
            'title',
            'instructions',
            'ratings',
            'servings',
            'prep_time',
            'cooking_time',
            'image',
        )

    def create(self, validated_data):
        """Create."""
        # Create Book without ingredients or tags
        tags_data = validated_data.pop('title')
        book = models.Book.objects.create(**validated_data)

        return book

    def update(self, instance, validated_data):
        
        instance.title = validated_data.get('title')
        instance.instructions = validated_data.get('instructions')
        instance.servings = validated_data.get('serve_with')
        instance.ratings = validated_data.get('ratings')
        instance.prep_time = validated_data.get('prep_time')
        instance.cooking_time = validated_data.get('cooking_time')
        instance.image = validated_data.get('image')

        instance.save()

        return instance
