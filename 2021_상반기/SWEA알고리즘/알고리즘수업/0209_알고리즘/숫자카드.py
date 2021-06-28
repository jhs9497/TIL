T = int(input())

for tc in range(T): # 테스트 갯수는 T로 주어진다고 하니깐 T input값으로
    Y = int(input())
    A = list(map(int, input()))

    A_count = [0] * 10

    for i in A:
        for j in range(len(A_count)):
            if i == j:
                A_count[j] += 1

    popular_number = 0
    popular_number_count = 0
    for a in range(len(A_count)):  # a를 0 ~ 9까지 돌리기 위해서
        if popular_number_count <= A_count[a]:
            popular_number = a
            popular_number_count = A_count[a]

    print('#{} {} {}'.format(tc+1, popular_number, popular_number_count))



