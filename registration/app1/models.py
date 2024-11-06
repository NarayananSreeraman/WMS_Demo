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

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='waste_requests')
    waste_type = models.CharField(max_length=20, choices=WASTE_TYPE_CHOICES)
    quantity = models.DecimalField(max_digits=5, decimal_places=2, help_text="Quantity in kg")
    scheduled_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"{self.user.username} - {self.waste_type} ({self.status})"

# Create your models here.
