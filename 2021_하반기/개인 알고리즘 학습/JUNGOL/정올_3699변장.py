for _ in range(int(input())):
    N = int(input())
    cloth_dict = {}
    cloth_list = []
    for _ in range(N):
        A, B = input().split()
        # 인풋받은 (의류, 종류)를 튜플형식으로 list에 추가!
        cloth_list.append((A, B))
    # 혹시 의류이름이 동일한 친구가 있을까 해서 set으로 중복제거 후 다시 리스트화
    cloth_list = set(cloth_list)
    cloth_list = list(cloth_list)


    for i in range(len(cloth_list)):
        # 만약 의류 종류가 cloth_dict에 이미 있으면 +1
        if cloth_list[i][1] in cloth_dict:
            cloth_dict[cloth_list[i][1]] += 1
        # 아직 없으면 초기값 2로! (안입는 경우도 산정해야하므로 초기값 2로 설정)
        else:
            cloth_dict[cloth_list[i][1]] = 2

    answer = 1
    for count in cloth_dict.values():
        # dict에서 의류종류별로 정리한 갯수를 차례로 곱하면서 답 구하기
        answer *= count
    # 마지막으로 -1한 후 출력
    answer -= 1

    print(answer)

