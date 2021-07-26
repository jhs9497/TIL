N = int(input())
ball = input()
red_count = ball.count('R')
blue_count = ball.count('B')

ans_count = min(red_count, blue_count)

# 정방향으로 체크
count = 0
for i in range(N):
    if ball[i] != ball[0]:
        break
    count += 1

if ball[0] == 'R':
    ans_count = min(ans_count, red_count - count)
else:
    ans_count = min(ans_count, blue_count - count)

# 역방향도 체크
reverse_count = 0
for i in range(N-1, -1, -1):
    if ball[i] != ball[-1]:
        break
    reverse_count += 1

if ball[-1] == 'R':
    ans_count = min(ans_count, red_count - reverse_count)
else:
    ans_count = min(ans_count, blue_count - reverse_count)

print(ans_count)

