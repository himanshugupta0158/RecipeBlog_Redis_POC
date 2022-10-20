from django.shortcuts import render
from django.views.generic import ListView, View
from django.http import HttpResponse

from django.core.cache import cache

from .models import *


class RecipesView(ListView):

    queryset = Recipe.objects.all()
    context_object_name = "recipes"
    template_name: str = "recipes/recipes.html"

    

class RecipeView(View):

    template_name : str = "recipes/recipe.html"

    def get(self, request, *args, **kwargs):
        print("id : ",kwargs["id"])
        id = kwargs['id']
        print(cache)

        if cache.get(id):
            recipe = cache.get(id)
            print("hit the cache")
        else:
            try:
                recipe = Recipe.objects.get(pk=id)
                cache.set(
                    recipe.id,
                    recipe
                )
                print("hit the DB")
            except Recipe.DoesNotExist:
                return HttpResponse("<h1> This recipe does not exist.</h1> ")

        # return HttpResponse("<h1>Details Page</h1> <br> recipe id :"+str(id))
        context = {
            "recipe" : recipe,
        }

        return render(
            request,
            self.template_name,
            context
        )

