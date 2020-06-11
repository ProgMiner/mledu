import datetime
import os

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

from ml import week5, week6, week7, week8, week9, week10, week12
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
            return render(request, 'week_5.html', context={'FIRST': FIRST,
                                                           'SECOND': SECOND,
                                                           'FIRD': FIRD,
                                                           'FORTH': FORTH,
                                                           'FITH': FITH})
        except Exception as ex:
            print(ex)
            return render(request, 'week_5.html', context={'error': 'Ошибка данных'})
        finally:
            os.remove(path)
            os.remove(path2)
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
        except Exception as ex:
            print(ex)
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
            return render(request, 'week_6-2.html', context={"t621": t621, "t622": t622, "t623": t623, "t624": t624,
                                                             "t625": t625, "t626": t626})
        except Exception as ex:
            print(ex)
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
        except Exception as ex:
            print(ex)
            return render(request, 'week_7.html', context={'error': 'Ошибка данных'})
    return render(request, 'week_7.html')


def week_81(request):
    if request.method == 'POST':
        try:
            return render(request, 'week_8-1.html', context=week8.week8_1(request.POST.get('data')))
        except Exception as ex:
            print(ex)
            return render(request, 'week_8-1.html', context={'error': 'Ошибка данных'})
    else:
        return render(request, 'week_8-1.html')


def week_82(request):
    if request.method == 'POST':
        try:
            return render(request, 'week_8-2.html', context=week8.week8_2(int(request.POST.get('count')),
                                                                          int(request.POST.get('train_part')),
                                                                          request.POST.get('criterion'),
                                                                          int(request.POST.get('max_leaf_nodes')),
                                                                          int(request.POST.get('min_samples_leaf')),
                                                                          int(request.POST.get('random_state')),
                                                                          request.POST.get('patients')))

        except Exception as ex:
            print(ex)
            return render(request, 'week_8-2.html', context={'error': 'Ошибка данных'})
    else:
        return render(request, 'week_8-2.html')


def week_9(request):
    if request.method == 'POST' and request.FILES['f']:
        x_1 = request.POST.get('x_1')
        x_2 = request.POST.get('x_2')
        x_3 = request.POST.get('x_3')
        y_1 = request.POST.get('y_1')
        y_2 = request.POST.get('y_2')
        y_3 = request.POST.get('y_3')
        myfile = request.FILES['f']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        path = fs.path(filename)
        try:
            answer, dist = week9.week9(path, x_1, y_1, x_2, y_2, x_3, y_3)
            return render(request, 'week_9.html', context={'answer': answer,
                                                           'dist': dist})
        except Exception as ex:
            print(ex)
            return render(request, 'week_9.html', context={'error': 'Ошибка данных'})
        finally:
            os.remove(path)
    else:
        return render(request, 'week_9.html')


def week_10(request):
    if request.method == 'POST':
        try:
            return render(request, 'week_10.html', context=week10.week10(float(request.POST.get('C')),
                                                                         int(request.POST.get('random_state')),
                                                                         request.POST.get('criterion'),
                                                                         int(request.POST.get('min_samples_leaf')),
                                                                         int(request.POST.get('max_leaf_nodes')),
                                                                         int(request.POST.get('n_estimators')),
                                                                         request.POST.get('solver'),
                                                                         int(request.POST.get('cv')),
                                                                         int(request.POST.get('class')),
                                                                         [i.strip() for i in
                                                                          request.POST.get('images').split(',')]))

        except Exception as ex:
            print(ex)
            return render(request, 'week_10.html', context={'error': 'Ошибка данных'})
    else:
        return render(request, 'week_10.html')


def week_11(request):
    return render(request, 'week_11.html')


def week_12(request):
    if request.method == 'POST':
        try:
            return render(request, 'week_12.html', context=week12.week12(float(request.POST.get('epsilon')),
                                                                         float(request.POST.get('gamma')),
                                                                         int(request.POST.get('random_seed'))))

        except Exception as ex:
            print(ex)
            return render(request, 'week_12.html', context={'error': 'Ошибка данных'})
    else:
        return render(request, 'week_12.html')
