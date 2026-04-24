from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add/', views.add_contact),
    path('edit/<int:id>/', views.edit_contact),
    path('delete/<int:id>/', views.delete_contact),
]