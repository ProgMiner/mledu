from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from ml import test


class GetAnswer(APIView):

    def get(self, request):
        data = test.test_alg()
        return Response({"data": data})

    def post(self, request):
        data = request.data.get('data')
        return Response({"success":"Nice"})

# Create your views here.
