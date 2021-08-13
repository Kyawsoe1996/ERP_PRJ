from rest_framework import parsers
from api.views import *
from .serializers import ProductSerializer
from product.models import *
from rest_framework import parsers

class ProductViewSet(viewsets.ModelViewSet):
    """
    List all books, or create a new book.
    """
    # parser_classes = [parsers.JSONParser,parsers.MultiPartParser]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

