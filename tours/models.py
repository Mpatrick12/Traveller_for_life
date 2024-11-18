from django.db import models
from accounts.models import User

class Location(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class Tour(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField()  # e.g., "3 days"
    tour_operator = models.ForeignKey(User, on_delete=models.CASCADE)
    available_slots = models.IntegerField()
    is_cultural_experience = models.BooleanField(default=False)
    image = models.ImageField(upload_to='tour_images/', null=True, blank=True)

    def __str__(self):
        return self.title

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now_add=True)
    booking_status = models.CharField(
        max_length=20,
        choices=[('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')],
        default='Confirmed'
    )
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.user.username} - {self.tour.title}'


# Create your models here.
