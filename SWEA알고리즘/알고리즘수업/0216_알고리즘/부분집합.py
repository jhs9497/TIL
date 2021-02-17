# arr = [1,2,3]
#
# n = len(arr)
#
# for i in range(1<<n): # 이 말은 1을 왼쪽으로 n칸 (즉 3칸) 가고 간 칸수를 0으로 바꾸는 것 즉 2진수로 1000(2) -> 8 결국 2의n승 이라는 뜻
#     # 8번 돌려보면서
#     for j in range(n): # 부분집합의 가짓수는 인덱스 0,1,2를 활용할테니 len(n)으로 표시
#         if i & (1<<j):
#             print(arr[j], end= ' ')
#     print()

test_case = int(input())

for tc in range(1, test_case+1):
    N, K = map(int, input().split())


    arr = [1,2,3,4,5,6,7,8,9,10,11,12]

    n = len(arr)

    set_list = []

    for i in range(1<<n):
        list_ = []
        for j in range(n):
            if i & (1<<j):
                list_ += [arr[j]]
        set_list += [list_]


    select_list = []
    for i in set_list:
        if len(i) == N :
            select_list += [i]

    count = 0

    for j in range(len(select_list)):
        total = 0
        for z in range(N):
            total += select_list[j][z]
        if total == K:
            count += 1
    print('#{} {}'.format(tc, count))



