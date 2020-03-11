from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from ml import week5
import datetime
import os
from .views import logs, get_client_ip
from .keys import KEYS



def del_key(key_to_del):
    KEYS.remove(int(key_to_del))
    print(len(KEYS))


def check_key(key):
    if int(key) in KEYS:
        return True
    else:
        return False


def week_5(request):
    logs.append([datetime.datetime.now().strftime("%m/%d, %H:%M"), get_client_ip(request)])
    if request.method == 'POST' and request.FILES['f']:
        try:
            KEY = request.POST.get('KEY')  # ПРОВЕРКА КЛЮЧА
            if not check_key(KEY):
                return render(request, 'week_5.html', context={'error': 'Ошибка ключа'})
            dc1 = request.POST.get('dc1')
            dc2 = request.POST.get('dc2')
            dc3 = request.POST.get('dc3')
            candy1 = request.POST.get('candy1')
            candy2 = request.POST.get('candy2')
            myfile = request.FILES['f']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            path = fs.path(filename)
            myfile_1 = request.FILES['f1']
            filename_1 = fs.save(myfile_1.name, myfile_1)
            path2 = fs.path(filename_1)
            try:
                FIRST, SECOND, FIRD, FORTH, FITH = week5.week5(path, path2, dc1, dc2, dc3, candy1, candy2)
                os.remove(path)
                os.remove(path2)
                del_key(KEY)  # УДАЛЕНИЕ КЛЮЧА
                return render(request, 'week_5.html', context={'FIRST': FIRST,
                                                               'SECOND': SECOND,
                                                               'FIRD': FIRD,
                                                               'FORTH': FORTH,
                                                               'FITH': FITH})
            except:
                os.remove(path)
                os.remove(path2)
                return render(request, 'week_5.html', context={'error': 'Ошибка данных'})
        except:
            return render(request, 'week_5.html', context={'error': 'Ошибка данных'})
    else:
        return render(request, 'week_5.html')


def week_6(request):
    return render(request, 'week_6.html')
