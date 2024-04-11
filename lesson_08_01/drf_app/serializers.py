from rest_framework import serializers

from .models import Author, Book, Publisher


def number_of_symbols_validator(value):
    if len(value) < 4:
        raise serializers.ValidationError("Длина должна быть больше 4 символов")
    return value


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, validators=[number_of_symbols_validator])

    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100, validators=[number_of_symbols_validator])
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, attrs):
        if len(attrs['description']) < 10:
            raise serializers.ValidationError("Слишком короткое описание")
        return attrs

    def create(self, validated_data):
        authors = validated_data.pop('authors')
        created_authors = []
        for author in authors:
            author, created = Author.objects.get_or_create(**author)
            created_authors.append(author)
        book = Book.objects.create(**validated_data)
        book.authors.set(created_authors)
        return book

    def update(self, instance: Book, validated_data):
        authors = validated_data.pop('authors')
        created_authors = []
        for author in authors:
            author, created = Author.objects.get_or_create(**author)
            created_authors.append(author)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.authors.set(created_authors)
        instance.save()
        return instance


