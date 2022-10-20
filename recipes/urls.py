from django.urls import path
from .views import RecipesView, RecipeView


urlpatterns = [
    path("", RecipesView.as_view(), name="recipes"),
    path("recipe/<int:id>", RecipeView.as_view(), name="recipe"),
]
