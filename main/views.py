from django.shortcuts import render, HttpResponse
from django.core.files.storage import FileSystemStorage
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from ml import week2
from ml import week3
from ml import week4
import datetime
from ml_server.settings import STATIC_URL
import os

logs = []

class Logs(APIView):
    def get(self, request):
        return Response({"logs": str(logs)})


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def week_2(request):
    logs.append([datetime.datetime.now().strftime("%m/%d, %H:%M"), get_client_ip(request)])
    if request.method == 'POST' and request.FILES['f']:
        try:
            star = request.POST.get('star')
            star = star.split(',')
            star = [float(st) for st in star]
            myfile = request.FILES['f']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            path = fs.path(filename)
            mean, min = week2.res(path, star)
            os.remove(path)
            return render(request, 'week_2.html', context={'mean': mean, 'min': min})
        except:
            return render(request, 'week_2.html', context={'error': 'Ошибка данных'})
    else:
        return render(request, 'week_2.html')


def week_3(request):
    logs.append([datetime.datetime.now().strftime("%m/%d, %H:%M"), get_client_ip(request)])
    if request.method == 'POST' and request.FILES['f']:
        try:
            myfile = request.FILES['f']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            path = fs.path(filename)
            myfile_1 = request.FILES['f1']
            filename_1 = fs.save(myfile_1.name, myfile_1)
            path_1 = fs.path(filename_1)
            myfile_2 = request.FILES['f2']
            filename_2 = fs.save(myfile_2.name, myfile_2)
            path_2 = fs.path(filename_2)
            try:

                FIRST, SECOND, FIRD, FORTH = week3.week3(path, path_1, path_2)
                os.remove(path)
                os.remove(path_1)
                os.remove(path_2)
                return render(request, 'week_3.html', context={'FIRST': FIRST,
                                                               'SECOND': SECOND,
                                                               'FIRD': FIRD,
                                                               'FORTH': FORTH})
            except:
                os.remove(path)
                os.remove(path_1)
                os.remove(path_2)
                return render(request, 'week_3.html', context={'error': 'Ошибка данных'})
        except:
            return render(request, 'week_3.html', context={'error': 'Ошибка данных'})
    else:
        return render(request, 'week_3.html')


def week_4_1(request):
    logs.append([datetime.datetime.now().strftime("%m/%d, %H:%M"), get_client_ip(request)])
    if request.method == 'POST' and request.FILES['f']:
        try:
            myfile = request.FILES['f']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            path = fs.path(filename)
            task_1, task_2, task_3, task_4, task_5 = week4.week_4_1(path)
            os.remove(path)
            return render(request, 'week_4.html', context={'task_1': task_1,
                                                           'task_2': task_2,
                                                           'task_3': task_3,
                                                           'task_4': task_4,
                                                           'task_5': task_5})
        except:
            return render(request, 'week_4.html', context={'error': 'Ошибка данных'})
    else:
        return render(request, 'week_4.html')


def week_4_2(request):
    logs.append([datetime.datetime.now().strftime("%m/%d, %H:%M"), get_client_ip(request)])
    if request.method == 'POST' and request.FILES['f']:
        try:
            myfile = request.FILES['f']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            path = fs.path(filename)
            array = request.POST.get('array')
            candy_1 = request.POST.get('candy_1')
            candy_2 = request.POST.get('candy_2')
            array = array.split(',')
            array = [float(st) for st in array]
            task_6, task_7, task_8 = week4.week4_2(path, candy_1, candy_2, array)
            os.remove(path)
            return render(request, 'week_4.html', context={'task_6': task_6,
                                                           'task_7': task_7,
                                                           'task_8': task_8})
        except:
            return render(request, 'week_4.html', context={'error': 'Ошибка данных'})
    else:
        return render(request, 'week_4.html')


def week_4(request):
    logs.append([datetime.datetime.now().strftime("%m/%d, %H:%M"), get_client_ip(request)])
    return render(request, 'week_4.html', context={'#': '#'})


def week_5(request):
    logs.append([datetime.datetime.now().strftime("%m/%d, %H:%M"), get_client_ip(request)])
    return render(request, 'week_5.html', context={'#': '#'})

