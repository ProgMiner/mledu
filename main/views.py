from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from ml import test


def index(request):
    return render(request, 'index.html')
# Create your views here.
