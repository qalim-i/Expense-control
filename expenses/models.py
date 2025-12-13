from django.db import models

from django.contrib.auth.models import User

class Expenses(models.Model):
    CATEGORY_CHOICES=[
        ('Rent', 'Rent'),
        ('Groceries', 'Groceries'),
        ('Transportation', 'Transportation'),
        ('Entertainment', 'Entertainment'),
        ('Miscellaneous', 'Miscellaneous'),
        ('Food', 'Food'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=120)
    category = models.CharField(max_length=120, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f'{self.title} - {self.amount}'

class Budget(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    limit_amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{self.user.username} - {self.limit_amount}'