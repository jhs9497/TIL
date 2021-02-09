test_case = int(input())

for tc in range(1, test_case+1):
    k, n, m = map(int, input().split())

    # k = 한번 충전으로 이동할 수 있는 거리
    # n = 가야할 총 거리
    # m = 전기 충전소 갯수

    X = list(map(int, input().split()))
    # X는 전기충전소 위치 인덱스 리스트

    Y = [n]

    Z = [0]

    X = Z + X + Y

    # 정류장 리스트에 정류장 총 길이 숫자 추가
    # 정류장 리스트에서 각 원소의 차가 k 보다 크면 0 반환

    # 정류장끼리의 거리가 k 보다 크면 X













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










