from django.urls import path
from .views import CartItemView
urlpatterns = [
    path('cart_items/', CartItemView.as_view()),
    path('cart_items/<int:id>/', CartItemView.as_view()),
]
