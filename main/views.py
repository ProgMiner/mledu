from django.shortcuts import render, HttpResponse
from django.core.files.storage import FileSystemStorage
from ml import week2
from ml import week3
import os


def week_2(request):
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
    if request.method == 'POST' and request.FILES['f']:
        try:
            myfile = request.FILES['f']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            path = fs.path(filename)
            # сделать проверку на расширение и на ввод данных
            FIRST, SECOND, FIRD, FORTH = week3.week3(path)
            os.remove(path)
            return render(request, 'week_3.html', context={'FIRST': FIRST,
                                                           'SECOND': SECOND,
                                                           'FIRD': FIRD,
                                                           'FORTH': FORTH})
        except:
            return render(request, 'week_3.html', context={'error': 'Ошибка данных'})
    else:
        return render(request, 'week_3.html')


def week_4(request):
    return render(request, 'week_4.html', context={'#': '#'})
# Create your views here.
