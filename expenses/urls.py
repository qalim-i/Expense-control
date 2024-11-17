from django.urls import path
from . import views

urlpatterns = [
    path('',views.expense_list, name='expense_list'),
    path("add/",views.add_expense, name ='add_expense'),
    path('edit/<int:expense_id>/', views.edit_expense, name='edit_expense'),
    path('delete/<int:expense_id>/', views.delete_expense, name='delete_expense'),
    # path('login', views.login_user,name='login'),
    # path('register', views.register,name='register'),
    # path('logout', views.logout_user,name='logout'),
]


