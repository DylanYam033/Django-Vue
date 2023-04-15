from rest_framework import viewsets
from .models import Book
from .serializer import BookSerializer

# Viewsets son clases que definen la funcionalidad de la vista para la API RESTful. Los Viewsets son una forma conveniente de agrupar las vistas relacionadas en un solo lugar y se utilizan para manejar las solicitudes HTTP para la API RESTful.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer