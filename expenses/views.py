from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Expenses
from django.http import HttpResponse
# from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.forms import AuthenticationForm
# from .forms import UserRegistrationForm

# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('expense_list')
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'register.html', {'form': form})

# def login_user(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             next_url = request.GET.get('next', '/')
#             return redirect(next_url) 
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})

# def logout_user(request):
#     logout(request)
#     return redirect('login')

def expense_list(request):
    category = request.GET.get('category')
    date = request.GET.get('date')
    expenses = Expenses.objects.all()
    if category:
        expenses = expenses.filter(category=category)
    if date:
        expenses = expenses.filter(date=date)
    return render(request, 'expense_list.html', {'expenses': expenses})

def add_expense(request):
    if request.method == 'POST':
        title = request.POST['title']
        amount = request.POST['amount']
        category = request.POST['category']
        date = request.POST['date']
        Expenses.objects.create(title=title, amount=amount, category=category, date=date)
        return redirect('expense_list')
    return render(request, 'add_expense.html')

def edit_expense(request,expense_id):
    expense = get_object_or_404(Expenses,id=expense_id)
    if request.method == 'POST' :
        expense.title = request.POST['title']
        expense.amount = request.POST['amount']
        expense.category = request.POST['category']
        expense.date = request.POST['date']
        expense.save()
        return redirect('expense_list')
    return render(request, 'edit_expense.html', {'expense': expense})

def delete_expense(request, expense_id):
    expense = get_object_or_404(Expenses, id=expense_id)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    return render(request, 'delete_expense.html', {'expense': expense})