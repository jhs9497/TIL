def solution(n):
    answer = ''
    while n > 0:
        n = n // 3
        a = n % 3
        print(n, a)


answer = solution(15)

print(answer)
