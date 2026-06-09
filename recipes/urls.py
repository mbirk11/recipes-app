from django.urls import path
from .views import (
    UserRegisterView,
    RecipeListCreateView,
    RecipeDetailView,
)

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("recipes/", RecipeListCreateView.as_view(), name="recipe-list-create"),
    path("recipes/<int:pk>/", RecipeDetailView.as_view(), name="recipe-detail"),
]