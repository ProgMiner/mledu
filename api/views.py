from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


class GetAnswer(APIView):
    @cors
    def get(self, request):
        data = 'test data'
        return Response({"data": data})

# Create your views here.
