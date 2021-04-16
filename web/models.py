from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Expense(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date.strftime('%m/%d/%Y')} {self.amount}"


class Income(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date.strftime('%m/%d/%Y')} {self.amount}"
