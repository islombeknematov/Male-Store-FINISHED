from django.urls import path

from api.views import CategoryListAPIView, ProductListAPIView

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view()),
    path('products/', ProductListAPIView.as_view()),
]
