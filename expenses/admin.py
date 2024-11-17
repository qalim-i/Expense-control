from django.contrib import admin
from .models import Expenses

@admin.register(Expenses)
class ExpensesAdmin(admin.ModelAdmin):
    list_display=("title","category","amount","date")
    list_filter=("category","date")
    search_fields=("ttile",'category')