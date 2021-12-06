from django.urls import path

from api.views import CategoryListAPIView, ProductListAPIView, ProductRetrieveAPIView

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view()),
    path('products/', ProductListAPIView.as_view()),

    path('products/<int:pk>/', ProductRetrieveAPIView.as_view()),
]

