x, y = map(int, input().split())

GCD = 0
LCM = 0

number = min(x, y)

while number > 0:
    if x % number == 0 and y % number == 0:
        GCD = number
        break
    number -= 1

LCM = (x*y) // GCD

print