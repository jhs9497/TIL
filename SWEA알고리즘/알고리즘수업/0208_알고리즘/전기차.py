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

    for t in range(len(X)-1):
        if X[t+1]-X[t] > k:
            print('#{} 0'.format(tc))
            break

    else:
        charge = 0
        start_point = 0
        while start_point < n:
            start_point += k
            for i in X:
                if start_point == i:
                    charge += 1
                else:
                    start_point -= (k+1)
        print(charge)