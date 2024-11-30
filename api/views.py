from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .serializers import ProductSerializer,ProductMiniSerializer
# Serializers define the API representation.
from .models import Product
from rest_framework.response import Response

# ViewSets define the view behavior.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        products = Product.objects.all()
        serializer = ProductMiniSerializer(products, many=True)
        return Response(serializer.data)