from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create_todo, name='create'),
    path('update/<int:pk>/', views.update_todo, name='update'),
    path('delete/<int:pk>/', views.delete_todo, name='delete'),
]


