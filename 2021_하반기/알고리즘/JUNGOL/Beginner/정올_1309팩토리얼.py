N = int(input())

answer = 1
while N > 0:
    if N > 1:
        answer *= N
        print(f'{N}! = {N} * {N-1}!')
    else:
        print(f'{N}! = {N}')
    N -= 1
print(answer)