from django.urls import path
from . import views

urlpatterns = [
    path('', views.payments_home, name='payments_home'),
    path('checkout/<int:booking_id>/', views.process_payment, name='process_payment'),
    path('payment-success/', views.payment_success, name='payment_success'),
    path('payment-failed/', views.payment_failed, name='payment_failed'),
]
