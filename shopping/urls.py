from django.urls import path
from . import views

urlpatterns = [
    path('lists/', views.ListsView.as_view()),
    path('list_detail/<int:pk>/', views.ListDetail.as_view()),
    path('categories/', views.Categories.as_view()),
    path('category_detail/<int:pk>/', views.CategoryDetail.as_view()),
]