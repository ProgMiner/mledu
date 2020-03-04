from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from ml import week2
import os

def week_2(request):
    if request.method == 'POST' and request.FILES['f']:
        star = request.POST.get('star')
        star = star.split(',')
        star = [float(st) for st in star]
        myfile = request.FILES['f']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        path = fs.path(filename)
        #сделать проверку на расширение и на ввод данных
        mean, min = week2.res(path, star)
        os.remove(path)
        return render(request, 'week_2.html', context={'mean': mean, 'min':min})
    else:
        return render(request, 'week_2.html')





def week_3(request):
    return render(request, 'week_3.html', context={'#': '#'})
# Create your views here.
