from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCreateView

urlpatterns = [
    path('api/products/', ProductListView.as_view()),
    path('api/products/<int:pk>/', ProductDetailView.as_view()),
    path('api/products/create/', ProductCreateView.as_view()),
]