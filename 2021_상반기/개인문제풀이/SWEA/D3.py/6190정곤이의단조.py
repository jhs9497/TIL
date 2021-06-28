def check(A):
    A_number = A
    A_list = []
    while A_number > 0:
        A_list.append(A_number%10)
        A_number = A_number // 10
    # 여기까지 A를 A_list에 거꾸로 집어 넣고
    # ex) A가 36이면 A_list에는 [6, 3]
    for i in range(len(A_list)-1):
        if A_list[i] < A_list[i+1]:
            return -1  # 단조인 수 가 없을 때 -1 출력해야함
    return A # 원래 수 리턴


for tc in range(1, int(input())+1):
    N = int(input())
    number = list(map(int, input().split()))

    sample = []
    # Ai X Aj의 모든 경우의 수 탐색
    for i in range(len(number)):
        for j in range(i+1, len(number)):
            A = number[i]*number[j] # 정답의 후보가 될 수 있는 수
            sample.append(check(A))

    print('#{} {}'.format(tc, max(sample)))