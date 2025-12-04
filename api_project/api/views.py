from rest_framework import generics
from .models import Book
from .serializers import BookSerializer   

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



# task 2
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
 
# final task
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  
    
    

