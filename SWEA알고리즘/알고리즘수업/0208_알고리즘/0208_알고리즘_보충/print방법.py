import sys
sys.stdin = open("1976.txt","r")

T = int(input())

for test_case in range(T):
    h1, m1, h2, m2 = map(int, input().split())

    # .format 스타일
    print("#{} {} {}".format(tc, h, m))

    # 반올림 해야할 때
    print("#{} {} {}".format(tc, h, int(m+0.5)))

    # c 스타일
    print("#%d %d %d" % (tc, h, m))

