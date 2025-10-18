from django.urls import path
from . import views

urlpatterns = [
    path('dimensions/', views.find_ships_dimensions, name="find_ships_dimensions"),
    path('dimensions/drawing/', views.generate_drawing, name="generate_drawing"),
    path('dimensions/drawing/numbers/', views.generate_drawing_with_numbers, name="generate_drawing_with_numbers"),
]