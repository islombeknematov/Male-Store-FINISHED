from rest_framework.generics import ListAPIView

from api.serializers import CategoryModelSerializer, ProductModelSerializer
from products.models import CategoryModel, ProductModel


class CategoryListAPIView(ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategoryModelSerializer


class ProductListAPIView(ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer

