import math

def check(number):
    if number == 1:
        print('number one')
        return    

    else:
        N = int(math.sqrt(number))
        for i in range(2, N+1):
            if number % i == 0:
                print('composite number')
                return
        
        print('prime number')
        return


number_list = list(map(int, input().split()))

for i in number_list:
    check(i)


