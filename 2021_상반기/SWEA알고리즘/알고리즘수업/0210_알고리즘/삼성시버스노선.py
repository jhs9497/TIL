test_case = int(input())

for tc in range(1, test_case+1):
    # 1~5000 까지의 버스정류장
    # 버스 노선은 N개
    N = int(input())
    # i번째 버스 노선은 정류장번호 Ai ~ Bi

    N_range = []  # 각 노선이 들리는 정류장 번호를 넣을 곳
    for i in range(1, N+1):
        Ai, Bi = map(int, input().split()) # Ai, Bi를 인풋으로 받으면서 범위를 알아내고
        for x in range(Ai, Bi+1): # 그 범위로 for문을 한 번 더 돌리면서
            N_range += [x] # N_range에 정류장번호별로 넣는다 ex) Ai = 1, Bi = 3이면
                           # 해당 노선은 1~3번의 정류장을 지난다는 뜻인데
                           # 이것을 풀어서 1,2,3 번의 정류장을 지난다고 N_range에 넣어준다
                           # why ? Cj랑 비교하려고
    P = int(input()) # 몇 개의 노선이 지난지 비교할 정류장의 갯수
    P_number = [] # input으로 받은 정류장 번호를 넣을 곳
    for j in range(1, P+1):
        Cj = int(input()) # 정류장 번호 받고 ( 무슨 번호가 올지는 모름 1~500일뿐 )
        P_number += [Cj] # 받은 정류장 번호를 P_number에 정렬해준다

    # 정류장 번호 알았고, 각 노선이 지나는 모든 정류장 번호를 알아냄
    # 각 노선이 같은 정류장을 두번 지나진 않기 때문에
    # 정류장 번호가 각 노선이 지나는 모든 정류장 번호에 몇 번 들어있나 확인하면 됨

    total_count = '' # 최종적으로 print할 값
    for a in P_number: # 인풋받은 정류장번호를 하나씩 돌면서
        a_count = 0
        for b in range(len(N_range)): # 인풋받은 노선이 지나는 모든 정류장을 인덱스로 돌면서
            if a == N_range[b]: # 만약 a 정류장 번호가 전체 정류장 리스트에서 마주치면
                a_count += 1 # count에 플러스 1

        total_count += str(a_count) # 한 줄로 뽑아야 하므로 str으로 더하기
        total_count += ' ' # 띄어쓰기 해야하므로 해주기

    print('#{} {}'.format(tc, total_count))
    # P개의 버스정류장에 대해 각 정류장에 몇 개의 버스노선이 다니는가