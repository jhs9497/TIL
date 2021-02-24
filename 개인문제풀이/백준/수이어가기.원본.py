N = int(input())

count = 0
answer = []
for i in range(1, N + 1):
    A = 0
    j = N - i
    n = N
    B = [n, i, j]
    while j >= 0:
        j = i - j
        i = n - i
        n = i + j
        A += 1
        B += [j]

    if count < A:
        count = A
        answer = B

answer_ = ''
for a in range(len(answer) - 1):
    answer_ += str(answer[a]) + ' '

print(count + 2)
print(answer_)