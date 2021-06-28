from django.shortcuts import render
import requests
import random

# Create your views here.
def pot(request):
    
    url = 'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=953'
    response = requests.get(url).json()
    answer = []
    answer.append(response['drwtNo1'])
    answer.append(response['drwtNo2'])
    answer.append(response['drwtNo3'])
    answer.append(response['drwtNo4'])
    answer.append(response['drwtNo5'])
    answer.append(response['drwtNo6'])
    bonus = response['bnusNo']

    x = ("{}+{}".format(answer, bonus))

    numbers = range(1, 46)

    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    nope = 0
    for i in range(1000):
        count = 0
        lotto = random.sample(numbers, 6)
        for j in lotto:
            if j in answer:
                count += 1
        
        if count == 6:
            one += 1
        elif count == 5:
            second = 0
            for k in lotto:
                if k == bonus:
                    second += 1
            
            if second > 0 :
                two += 1
            else:
                three += 1

        elif count == 4:
            four += 1
        
        elif count == 3:
            five += 1

        else:
            nope += 1

        context = {
            'x' : x,
            'one' : one,
            'two' : two,
            'three' : three,
            'four' : four,
            'five' : five,
            'nope' : nope,
        }


    return render(request, 'lotto/pot.html', context)
