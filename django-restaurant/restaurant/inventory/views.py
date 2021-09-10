from django.shortcuts import render
from django.db.models import Sum
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from .forms import IngredientForm, MenuForm, PurchaseForm, RecipeForm

# Create your views here.
class HomeView(TemplateView):
  template_name = "inventory/home.html"

  def get_context_data(self):
    context = super().get_context_data()
    context["ingredients"] = Ingredient.objects.all()
    context["menus"] = MenuItem.objects.all()
    context["purchases"] = Purchase.objects.all()
    return context

class IngredientView(ListView):
    model = Ingredient
    template_name = "inventory/ingredient.html"

class CreateIngredientView(CreateView):
    model= Ingredient
    template_name = "inventory/ingredient_create.html"
    form_class = IngredientForm

class UpdateIngredientView(UpdateView):
    model = Ingredient
    template_name = "inventory/ingredient_update.html"
    form_class = IngredientForm

class DeleteIngredientView(DeleteView):
    model = Ingredient
    template_name = "inventory/ingredient_delete.html"
    success_url = "/ingredients/"

##############################################
###########      MenuItem Views        #######
##############################################

class MenuItemView(ListView):
    model = MenuItem
    template_name = "inventory/menu_item.html"

class CreateMenuView(CreateView):
    model= MenuItem
    template_name = "inventory/menu_create.html"
    form_class = MenuForm

class UpdateMenuView(UpdateView):
    model = MenuItem
    template_name = "inventory/menu_update.html"
    form_class = MenuForm

class DeleteMenuView(DeleteView):
    model = MenuItem
    template_name = "inventory/menu_delete.html"
    success_url = "/menus/"

# missing createview, update, delete

class PurchaseView(ListView):
    model = Purchase
    template_name = "inventory/purchase.html"

class CreatePurchaseView(CreateView):
    model = Purchase
    template_name = "inventory/add_purchase.html"
    form_class = PurchaseForm

class NewRecipeRequirementView(CreateView):
    template_name = "inventory/add_recipe_requirement.html"
    model = RecipeRequirement
    form_class = RecipeForm

class ReportView(TemplateView):
    template_name = "inventory/reports.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["purchases"] = Purchase.objects.all()
        revenue = Purchase.objects.aggregate(
            revenue=Sum("menu_item__price"))["revenue"]
        total_cost = 0
        for purchase in Purchase.objects.all():
            for recipe_requirement in purchase.menu_item.reciperequirement_set.all():
                total_cost += recipe_requirement.ingredient.unit_price * \
                    recipe_requirement.quantity

        context["revenue"] = revenue
        context["total_cost"] = total_cost
        context["profit"] = revenue - total_cost

        return context