from django.shortcuts import render
from .models import Expense, Income


def index(request):
    return render(request, "web/home.html", {"Expenses": Expense.objects.all(), "Incomes": Income.objects.all()})
