# 심는 나무 갯수는 for문으로 2씩 띄어가며 count를 하자
# 가장비싼 나무의 가격과 열은 마찬가지로 for문을 돌리면서 가장 큰 값을 찾아내자

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    garden = [list(map(int, input().split())) for _ in range(N)] # tc마다 설정된 garden

    cost = 0 # 총 비용
    count = 0 # 심은 나무의 수
    expensive = 0 # 가장 비싼 나무
    ex_idx = 0 # 가장 비싼 나무의 열

    for i in range(0, M, 2): # 열은 처음부터 시작해서 한 칸 씩 띄어서 돌기
        for j in range(N): # 행은 다 돌기
            cost += garden[j][i] # garden에 설정된 나무 가격 인덱스로 추가
            count += 1 # j 하나씩 돌릴 때 마다 나무 수 추가
            if expensive <= garden[j][i]: # for문 돌면서 가장 비싼 나무를 찾으면 (중복일 경우 뒤에 열이 나오도록 <=)
                expensive = garden[j][i] # expensive에 그 가격 입력되게 하고
                ex_idx = i+1 # 해당하는 열 추가 ( 인덱스는 0부터 시작이므로 1 추가 )


    print('# {} {} {} {} {}'.format(tc, cost, count, expensive, ex_idx))

