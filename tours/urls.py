from django.urls import path
from . import views

urlpatterns = [
    path('', views.tour_list, name='tour_list'),
    path('<int:tour_id>/', views.tour_detail, name='tour_detail'),
    path('<int:tour_id>/book/', views.book_tour, name='book_tour'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('operator/dashboard/', views.operator_dashboard, name='operator_dashboard'),
    path('search/', views.search, name='search'),  # Add this line
]
