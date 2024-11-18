from django.db import models
from accounts.models import User
from tours.models import Booking

class Payment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=20,
        choices=[('Completed', 'Completed'), ('Failed', 'Failed')],
        default='Completed'
    )
    transaction_id = models.CharField(max_length=100, unique=True)

# Create your models here.
