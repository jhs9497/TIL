for tc in range(1, int(input())+1):
    # 우선 다루기 쉽게 리스트로 바꾼다
    rough = input()
    rough_list = []
    for r in range(len(rough)):
        rough_list += [rough[r]]

    # 레이져들을 찾아내보자
    # 레이져는 원소 2개로 이루어져 있으니 2칸씩 완전탐색
    razer_index = []
    for i in range(len(rough)-1):
        A = rough[i] + rough[i+1]
        if A == '()': # rough 스트링열에서 ()를 찾았고 그 인덱스에 해당하는 () 를 번호로 바꾸어서 레이져에 번호를 달아주자
            # 우선 해당하는 인덱스를 뽑아내자
            razer_index += [i]

    # 구한 razer_index를 이용해서 rough 스트링렬을 레이져번호가 쓰여진 스트링열으로 변환
    for a in range(len(razer_index)):  # ex) a : 0~5 = 0,5,7,11,14,19
        rough_list[razer_index[a]] = a
        rough_list[razer_index[a]+1] = a

    # 번호기준으로 왼쪽에 ((((의 갯수와 오른쪽의 )))) 갯수중 더 많은 것이 한 레이져가 부수는 쇠막대기 갯수임
    # 주의 레이져가 지금 11 이런식으로 번호가 매겨져 있기 때문에
    # 왼쪽은 정상대로 탐색을 하되 오른쪽은 인덱스 추가하고 탐색 시작해야함

    answer = [0]*len(razer_index) # 최종 정답

    left_answer = [0]*len(razer_index) # 왼쪽 탐색
    for x in range(len(razer_index)): # 0, 1, 2, 3, 4, 5 순으로 나옴
        Y = razer_index[x] -1
        y = Y

        while y >= 0 and y <= len(rough_list) and rough_list[y] == '(':
            left_answer[x] += 1
            y -= 1

    print(left_answer)

    # 오른쪽 탐색

    right_answer = [0]*len(razer_index)

    for x in range(len(razer_index)): # 0, 1, 2, 3, 4, 5 순으로 나옴
        Y = razer_index[x]+2 # 한칸 더 띄어야함
        y = Y
        while y <= len(rough_list) and y >= 0  and rough_list[y] == ')':
            right_answer[x] += 1
            y += 1
    if answer[x] < right_answer[x]:
        answer[x] = right_answer[x]

    print(right_answer)



