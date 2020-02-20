from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from ml import test
from ml.test import Test


class GetAnswer(APIView):

    def get(self, request):
        data = Test.test_alg()
        return Response({"data": data})

    def post(self, request):
        data = request.data.get('data')
        GetAnswer.save(data)
        return Response({"success": "nice"})

    @staticmethod
    def save(data):
        Test.data = data

# Create your views here.
