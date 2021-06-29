def gcd_get(x, y):
    for i in range(x, 0, -1):
        if x % i == 0 and y % i == 0:
            return i

N = int(input())
number_list = list(map(int, input().split()))
number_list.sort()

GCD = LCM = number_list[0]

for i in range(1, N):
    GCD = gcd_get(GCD, number_list[i])
    LCM = int(LCM/gcd_get(LCM, number_list[i])*number_list[i])

print(GCD, LCM)
