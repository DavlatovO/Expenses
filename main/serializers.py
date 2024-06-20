
from rest_framework import serializers
from .import models

class ExpenseSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Expense
        fields = ['user', 'title', 'description', 'amount', 'date']



        