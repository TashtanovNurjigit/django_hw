from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_view, name='book'),
    path('book_details/<int:id>/', views.book_details_view, name='details'),
]
