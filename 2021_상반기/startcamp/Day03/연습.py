import random

lotto_now = [1,3,4,5,6,8]
bonus = 14

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
        if j in lotto_now:
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


print(one, two, three, four, five, nope)