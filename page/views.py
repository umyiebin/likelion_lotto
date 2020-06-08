from django.shortcuts import render
import random as r

# Create your views here.

def home(request):
    return render(request, 'home.html')

def result(request):
    count = 0
    number_list = []
    random_list = []

    # 입력한 번호
    for i in range(1, 7):
        num = request.GET['number%d' % i]
        number_list.append(num)

    # 당첨번호
    while len(random_list) < 6:
        random_num = r.randrange(1,46)
        if random_num in random_list:
            continue
        else:
            random_list.append(random_num)
    
    # 맞춘 개수 확인하기
    for i in range(len(number_list)):
        for j in range(len(random_list)):
            if number_list[i] == random_list[j]:
                count += 1

    return render(request, 'result.html', {'number_list':number_list, 'random_list':random_list, 'count':count})