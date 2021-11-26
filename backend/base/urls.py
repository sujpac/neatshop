from django.urls import path
from . import views
from .views import MyTokenObtainPairView

urlpatterns = [
    path('', views.get_routes, name='routes'),
    path('products/', views.get_products, name='products'),
    path('products/<str:pk>/', views.get_product, name='product'),
    path('users/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
