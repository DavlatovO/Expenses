from django.shortcuts import render
from django.shortcuts import render
from .import models
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import ExpenseSerializers
from rest_framework import generics, mixins, viewsets
from rest_framework.decorators import action








class ExpenseViewset(viewsets.ModelViewSet):
    queryset = models.Expense.objects.all()
    serializer_class = ExpenseSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]
