from django.urls import path
from . import views

urlpatterns = [
    #path("", views.index, name='index'),
    path('books/list/', views.book_list, name='book_list'),
    path('books/create/', views.book_create, name='book_create'),
    path('books/update/<int:pk>/', views.book_update, name='book_update'),
    path('books/delete/<int:pk>/', views.book_delete, name='book_delete'),
]
