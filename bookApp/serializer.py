from rest_framework import serializers
from .models import Book

# este archivo define cómo se convierten los modelos y otros tipos de datos en un formato que pueda ser transferido a través de una API web.

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
