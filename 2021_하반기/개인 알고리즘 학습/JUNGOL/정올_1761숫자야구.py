import itertools

def check(now_number):
    global number
    global strike
    global ball

    for i in range(len(number)):
        is_strike = 0
        is_ball = 0
        for j in range(3):
            if str(now_number[j]) == number[i][j]:
                is_strike += 1
            elif str(now_number[j]) in number[i]:
                is_ball += 1

        if strike[i] != is_strike or ball[i] != is_ball:
            return 0
    return 1

number = []
strike = []
ball = []
for _ in range(int(input())):
    n, s, b = map(int, input().split())
    number.append(str(n))
    strike.append(s)
    ball.append(b)

cand = list(itertools.permutations(range(1, 10), 3))

count = 0
for i in range(len(cand)):
    now_number = cand[i]
    count += check(now_number)
print(count)