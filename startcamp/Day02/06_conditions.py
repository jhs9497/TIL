n = 10

# 1. 주어진 양수 n이 홀수, 짝수인지 판별하여 출력하는 코드를 작성하시오.
# (hint) 05_operattor에서 배운 나머지 연산자를 사용해보면 어떨까요?

# 어떤 수를 2로 나눴을 때, 나머지가 0이면 짝수, 아니면 홀수

if n % 2 == 0 :
    print('n은 짝수')
else :
    print('n은 홀수')

# 2. 주어진 숫자 n이 양수, 0, 음수인지 판별하여 출력하는 코드를 작성하시오.

n = -4
if n > 0 :
    print('n은 양수')
elif n < 0 :
    print('n은 음수')
else : 
    print('n은 0')