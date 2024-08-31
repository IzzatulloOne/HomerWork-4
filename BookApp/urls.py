from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/<int:id>/', views.book_detail, name='book_detail'),
    path('add/', views.add_book, name='add_book'),
    path('page_one/', views.page_one, name='page_one'),
    path('page_two/', views.page_two, name='page_two'),
    path('page_three/', views.page_three, name='page_three'),
]
