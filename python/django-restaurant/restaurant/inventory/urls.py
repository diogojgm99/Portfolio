from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('ingredients/', views.IngredientView.as_view(), name="ingredients"),
    path('ingredients/create/', views.CreateIngredientView.as_view(), name="create_ingredient"),
    path('ingredients/<pk>/update/', views.UpdateIngredientView.as_view(), name="update_ingredient"),
    path('ingredients/<pk>/delete/', views.DeleteIngredientView.as_view(), name="delete_ingredient"),
    path('menu_item/', views.MenuItemView.as_view(), name="menus"),
    path('menu_item/create/', views.CreateMenuView.as_view(), name="create_menu"),
    path('menu_item/<pk>/update/', views.UpdateMenuView.as_view(), name="update_menu"),
    path('menu_item/<pk>/delete/', views.DeleteMenuView.as_view(), name="delete_menu"),
    path('purchases/', views.PurchaseView.as_view(), name = "purchases"),
    path('purchases/new/',views.CreatePurchaseView.as_view(), name="add_purchase"),
    path('reciperequirement/new/', views.NewRecipeRequirementView.as_view(), name="add_recipe_requirement"),
    path('reports/', views.ReportView.as_view(), name="reports"),
]