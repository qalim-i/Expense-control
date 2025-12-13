from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Expenses, Budget
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm, BudgetForm, StyledAuthForm
from django.db.models import Sum
from datetime import date as dt

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password) # Hash password
            user.save()
            login(request, user)
            return redirect('expense_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = StyledAuthForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next', 'expense_list')
            return redirect(next_url) 
    else:
        form = StyledAuthForm()
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def expense_list(request):
    category = request.GET.get('category')
    date_filter = request.GET.get('date')
    
    expenses = Expenses.objects.filter(user=request.user).order_by('-date')
    
    if category:
        expenses = expenses.filter(category=category)
    if date_filter:
        expenses = expenses.filter(date=date_filter)
        
    # Budget Logic
    budget = Budget.objects.filter(user=request.user).first()
    total_spent = 0
    remaining = 0
    percentage = 0
    
    if budget:
        # Filter expenses within budget range
        relevant_expenses = expenses.filter(date__range=[budget.start_date, budget.end_date])
        total_spent = relevant_expenses.aggregate(Sum('amount'))['amount__sum'] or 0
        remaining = budget.limit_amount - total_spent
        if budget.limit_amount > 0:
            percentage = (total_spent / budget.limit_amount) * 100
            
    context = {
        'expenses': expenses,
        'budget': budget,
        'total_spent': total_spent,
        'remaining': remaining,
        'percentage': min(percentage, 100), # Cap for bar width
        'over_budget': percentage > 100
    }
    return render(request, 'expense_list.html', context)

@login_required(login_url='login')
def add_expense(request):
    if request.method == 'POST':
        title = request.POST['title']
        amount = request.POST['amount']
        category = request.POST['category']
        date = request.POST['date']
        Expenses.objects.create(user=request.user, title=title, amount=amount, category=category, date=date)
        return redirect('expense_list')
    return render(request, 'add_expense.html')

@login_required(login_url='login')
def edit_expense(request,expense_id):
    expense = get_object_or_404(Expenses, id=expense_id, user=request.user)
    if request.method == 'POST' :
        expense.title = request.POST['title']
        expense.amount = request.POST['amount']
        expense.category = request.POST['category']
        expense.date = request.POST['date']
        expense.save()
        return redirect('expense_list')
    return render(request, 'edit_expense.html', {'expense': expense})

@login_required(login_url='login')
def delete_expense(request, expense_id):
    expense = get_object_or_404(Expenses, id=expense_id, user=request.user)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    return render(request, 'delete_expense.html', {'expense': expense})

@login_required(login_url='login')
def set_budget(request):
    try:
        budget = Budget.objects.get(user=request.user)
    except Budget.DoesNotExist:
        budget = None
        
    if request.method == 'POST':
        form = BudgetForm(request.POST, instance=budget)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            return redirect('expense_list')
    else:
        form = BudgetForm(instance=budget)
    return render(request, 'set_budget.html', {'form': form})