N, B = map(int, input().split())

# 16진수에 쓸 문자리스트
alpha = ['A', 'B', 'C', 'D', 'E', 'F']

answer = ''
while N > 0:
    # N을 B로 나눈것의 나머지를 계속 앞에다가 붙혀주면됨!
    number = N % B
    # 근데 만약 number가 10보다 크면 (16진수이면)
    if number >= 10:
        # number는 alpha에 만들어놓은 문자리스트에서 뽑아가기
        # number가 11이면 alpha[11-10] -> B
        number = alpha[number-10]

    # answer 앞에다가 붙혀주기!
    answer = str(number) + answer
    # N은 몫만 남기기
    N = N // B

print(answer)

