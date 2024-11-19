from django.db import models
from django.contrib.auth.models import User

class WasteRequest(models.Model):
    WASTE_TYPE_CHOICES = [
        ('plastic', 'Plastic'),
        ('organic', 'Organic'),
        ('electronic', 'Electronic'),
        ('metal', 'Metal'),
        ('other', 'Other'),
    ]
    ROUTE_CHOICES = [
        ('Route1', 'Route1'),
        ('Route2', 'Route2'),
        ('Route3', 'Route3'),
        ('Route4', 'Route4'),
        ('Route5', 'Route5'),
        ('Route6', 'Route6'),
    ]

    waste_type = models.CharField(max_length=100)
    quantity = models.FloatField()
    scheduled_time = models.DateTimeField()
    location = models.CharField(max_length=200)
    status = models.CharField(max_length=50, default='Pending')
    route = models.CharField(max_length=10, choices=ROUTE_CHOICES, default='TBL')
    


    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='waste_requests')
    waste_type = models.CharField(max_length=20, choices=WASTE_TYPE_CHOICES)
    quantity = models.DecimalField(max_digits=5, decimal_places=2, help_text="Quantity in kg")
    scheduled_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"{self.user.username} - {self.waste_type} ({self.status})"

# Create your models here.
