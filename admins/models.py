# admins/models.py
from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    specialization = models.CharField(max_length=255)
    experience = models.IntegerField()
    password = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    client_name = models.CharField(max_length=255)
    feedback_text = models.TextField()
    numerical_rating = models.IntegerField()

    # Add any other fields as needed
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} - {self.numerical_rating}"
