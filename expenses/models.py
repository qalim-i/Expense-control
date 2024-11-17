from django.db import models

class Expenses(models.Model):
    CATEGORY_CHOICES=[
        ('Rent', 'Rent'),
        ('Groceries', 'Groceries'),
        ('Transportation', 'Transportation'),
        ('Entertainment', 'Entertainment'),
        ('Miscellaneous', 'Miscellaneous'),
        ('Food', 'Food'),
    ]
    title = models.CharField(max_length=120)
    category = models.CharField(max_length=120, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f'{self.title} - {self.amount}'