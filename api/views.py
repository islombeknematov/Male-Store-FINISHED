from rest_framework.generics import ListAPIView, RetrieveAPIView

from api.serializers import CategoryModelSerializer, ProductModelSerializer
from products.models import CategoryModel, ProductModel


class CategoryListAPIView(ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategoryModelSerializer


class ProductListAPIView(ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer


class ProductRetrieveAPIView(RetrieveAPIView):  # DetailAPIView ==> Rest ==> RetrieveAPIView
    serializer_class = ProductModelSerializer
    queryset = ProductModel.objects.all()

