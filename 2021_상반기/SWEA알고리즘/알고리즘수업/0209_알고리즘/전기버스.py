test_case = int(input())

for tc in range(1, test_case+1):
    k, n, m = map(int, input().split())

    # k = 한번 충전으로 이동할 수 있는 거리
    # n = 가야할 총 거리
    # m = 전기 충전소 갯수

    X = list(map(int, input().split()))
    # X는 전기충전소 위치 인덱스 리스트

    point = 0
    charge = 0
    charge_distance = 0

    while point < n :  # point가 전체 길이보다 작은 동안 계속 실행

        point += k  # 일단 갈 수있는 k만큼 쭉 가고
        if point < n:


            step_back = 0 # 충전소가 없을 시 뒤로 백할 카운팅변수
            for i in range(point, point-k, -1): # 내가 k만큼 간 포인트부터 거꾸로 하나씩 충전소가 있나 살펴보면서
                if i in X: # 만약 충전소가 있으면
                    charge += 1 # charge 횟수에 +1 하고
                    point -= step_back # point는 내가 스텝백한 수 만큼 뒤로 무른다
                    break # 한 번 했으니 그만!
                else:
                    step_back += 1 # 만약 충전소가 없으면 뒤로 가야하므로 스텝백 +1 해준다

            if step_back == k: # 만약 step_back이 k만큼 커지면
                charge_distance = step_back # charge_distance에 넣기
    if charge_distance == k: # charge_distance가 k만큼이면 안되므로
        print("#{} 0".format(tc)) # 0 출력
    else: # 그게 아니면
        print("#{} {}".format(tc, charge)) # 쌓여있는 charge 출력















        # for a in range(0, n, k):  # 가야할 총 거리를 k칸씩 간다고 생각 일단 갈수 있는 최대한 가고!
        #     print(a)
        # #     for b in range(a, a-k, -1):  # 일단 지른 거리에 정류장 있으면 땡큐고 아니면 앞으로 한칸씩 가며
        # #     # k가 3이라면 b = 3,2,1  /  6,5,4  /  9,8,7 순으로 정류장 확인, 결국 항상 최대한 멀리 있는 정류장서 주유하게 됨
        # #         for c in X:  # 정류장 리스트를 돌리면서
        # #             if b == c:
        # #                 charge += 1
        # #             break
        # #
        # # print(charge)








    #     count = n // k
    #
    #     if count > m:
    #         print('#{} 0'.format(tc))
    #     else:
    #         print('#{} {}'.format(tc, count))



        # count = 0
        # for j in range(k, n+1, k):
        #
        #     if k % 2 == 0 :  # k가 짝수일때
        #         for p in range(j-(k//2)-1, j+1): #k가 6일때 j가 6이면 3~6까지, j가 12이면 9~12까지
        #
        #                 if p in X:
        #
        #                     count +=1
        #                     break
        #
        #     else:  # k가 홀수일때
        #         for p in range(j-(k//2), j+1): #k가 5일때 j가 5면 2~5까지  # j가 두번째 바퀴에서 10이면 7~10까지
        #
        #
        #                 if p in X:
        #
        #                     count +=1
        #                     break










