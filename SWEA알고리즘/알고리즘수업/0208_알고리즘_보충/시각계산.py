import sys
sys.stdin = open("1976.txt","r")

T = int(input())

for test_case in range(T):
    h1, m1, h2, m2 = map(int, input().split())

    h = h1 + h2
    m = m1 + m2

    carry = m // 60         # 올림수로 몫을 구하자
    m = m % 60              # 나머지로 분을 구하자
    h += carry

    if h % 12 == 0 and h > 0:
        h = 12
    else:
        h %= 12
    print("#{} {} {}".format(test_case+1, h, m))