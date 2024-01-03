from django.urls import path
from . import views



urlpatterns = [
    path('books', views.BookView.as_view()),
    path('books/<int:pk>', views.SingleBookView.as_view()),
    # path('books', views.books), 
    # path('numbers', views.display_even_numbers),
]

