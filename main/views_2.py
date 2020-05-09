from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from ml import week5, week6, week7, week8
import datetime
import os
from .views import logs, get_client_ip


def week_5(request):
    logs.append([datetime.datetime.now().strftime("%m/%d, %H:%M"), get_client_ip(request)])
    if request.method == 'POST' and request.FILES['f']:
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
            return render(request, 'week_5.html', context={'FIRST': FIRST,
                                                           'SECOND': SECOND,
                                                           'FIRD': FIRD,
                                                           'FORTH': FORTH,
                                                           'FITH': FITH})
        except:
            os.remove(path)
            os.remove(path2)
            return render(request, 'week_5.html', context={'error': 'Ошибка данных'})
    else:
        return render(request, 'week_5.html')


def week_61(request):
    if request.method == 'POST':
        spam = request.POST.get('spam').split(',')
        for i in range(0, len(spam)):
            spam[i] = int(spam[i])
        ham = request.POST.get('ham').split(',')
        for i in range(0, len(ham)):
            ham[i] = int(ham[i])
        email = request.POST.get('email').split(',')
        for i in range(0, len(email)):
            email[i] = int(email[i])
        words = request.POST.get('words').split(',')
        for i in range(0, len(words)):
            words[i] = int(words[i])
        words_to_num = request.POST.get('words_to_num').split(',')
        for i in range(0, len(words_to_num)):
            words_to_num[i] = int(words_to_num[i])
        try:
            t611, t612, t613, t614 = week6.week6_1(spam, ham, email, words, words_to_num)
            return render(request, 'week_6-1.html', context={"t611": t611, "t612": t612, "t613": t613, "t614": t614})
        except Exception:
            return render(request, 'week_6-1.html', context={'error': 'Ошибка данных'})
    return render(request, 'week_6-1.html')


def week_62(request):
    if request.method == 'POST':
        x_0 = request.POST.get('x_0').split(',')
        for i in range(0, len(x_0)):
            x_0[i] = int(x_0[i])
        y_0 = request.POST.get('y_0').split(',')
        for i in range(0, len(y_0)):
            y_0[i] = int(y_0[i])
        cl = request.POST.get('cl').split(',')
        for i in range(0, len(cl)):
            cl[i] = int(cl[i])
        obj = request.POST.get('obj').split(',')
        for i in range(0, len(obj)):
            obj[i] = int(obj[i])
        try:
            t621, t622, t623, t624, t625, t626 = week6.week6_2(x_0, y_0, cl, obj)
            return render(request, 'week_6-2.html', context={"t621": t621, "t622": t622, "t623": t623, "t624": t624
                , "t625": t625, "t626": t626})
        except Exception:
            return render(request, 'week_6-2.html', context={'error': 'Ошибка данных'})
    return render(request, 'week_6-2.html')


def week_7(request):
    if request.method == 'POST':
        rand = request.POST.get('rand')
        c = request.POST.get('c')
        t1 = request.POST.get('t1')
        t2 = request.POST.get('t2')
        t3 = request.POST.get('t3')
        images = request.POST.get('images').split(',')
        try:
            a1, a2, a3, a4, a5 = week7.week7(rand, c, t1, t2, t3, images)
            return render(request, 'week_7.html', context={"a1": a1, "a2": a2, "a3": a3, "a4": a4, "a5": a5})
        except Exception as exept:
            print(exept)
            return render(request, 'week_7.html', context={'error': 'Ошибка данных'})
    return render(request, 'week_7.html')


def week_8(request):
    return render(request, 'week_8.html')


def week_9(request):
    return render(request, 'week_9.html')
