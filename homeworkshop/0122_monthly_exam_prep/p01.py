'''
N 까지의 총합

정수 num을 기준으로, 1~num까지의 총 합을 반환하는 함수를

1. `for` 문을 사용하여 작성하시오.
2. `while`문을 사용하여 작성하시오.

---
[입력 예시]
4

[출력 예시]
10
'''

# for문만 사용하여 풀기
def sum_with_for(num):
    total = 0
    for i in range(1, num+1):
        total += i
    return total

sum_with_for(4)


# while문만 사용하여 풀기
def sum_with_while(num):
    i = 1
    while i <= num:
        i += num
    return i


sum_with_for(4)


# 아래 코드는 바꾸지 않습니다.
if __name__ == '__main__':
    print(sum_with_for(4))    # 10
    print(sum_with_while(4))  # 10
    print(sum_with_for(5))    # 15
    print(sum_with_while(5))  # 15