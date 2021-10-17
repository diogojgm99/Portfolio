from django.shortcuts import render, redirect
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

class CreatePurchaseView(TemplateView):
    #model = Purchase
    template_name = "inventory/add_purchase.html"
    #form_class = PurchaseForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu_items"] = [X for X in MenuItem.objects.all() if X.available()]
        return context

    def post(self, request):
        menu_item_id = request.POST["menu_item"]
        menu_item = MenuItem.objects.get(pk=menu_item_id)
        requirements = menu_item.reciperequirement_set
        purchase = Purchase(menu_item=menu_item)

        for requirement in requirements.all():
            required_ingredient = requirement.ingredient
            required_ingredient.quantity -= requirement.quantity
            required_ingredient.save()

        purchase.save()
        return redirect("/purchases")
    

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