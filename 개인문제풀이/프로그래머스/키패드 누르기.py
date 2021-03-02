def solution(numbers, hand):
    answer = ''
    keypad = [[1, 2, 3],[4, 5, 6],[7, 8, 9],['*', 0, '#']]  # keypad 2차원배열로 표현


    left_idx = [3, 0]  # 초기 * 인덱스
    right_idx = [3, 2] # 초기 # 인덱스
    for i in numbers: # 인풋 받은 numbers를 돌면서
        for j in range(4): # 행
            for k in range(3): # 렬
                if i == keypad[j][k] and (i == 1 or i == 4 or i == 7): # 만약 i값이 keypad[j][k]랑 같으면서 왼쪽에 있으면~
                    answer += 'L' # answer에 'L'추가하고
                    left_idx[0] = j # left_idx 현재 위치 인덱스로 바꿔주기
                    left_idx[1] = k
                    break

                elif i == keypad[j][k] and (i == 3 or i == 6 or i == 9):  # 오른쪽도 마찬가지
                    answer += 'R'
                    right_idx[0] = j
                    right_idx[1] = k
                    break

                elif i == keypad[j][k] and (i == 2 or i == 5 or i == 8 or i == 0): # 만약 2580 이면
                    L1 = abs(int(j) - left_idx[0]) # int는 안해도 될거 같은데 왜했지 ?
                    L2 = abs(int(k) - left_idx[1]) # 2580에 해당하는 인덱스에서 (j,k) left_idx의 현재 인덱스 (((x,y)라 치고))를
                                                   # 각각 빼줘서 거리를 구한다. 음수가 나올수 있으니 절대값 처리

                    R1 = abs(int(j) - right_idx[0]) # R1도 마찬가지
                    R2 = abs(int(k) - right_idx[1])

                    if L1 + L2 < R1 + R2: # 손꾸락은 상하좌우밖에 못움직이므로 각각을 더한것을 비교하면 된다
                        answer += 'L'
                        left_idx[0] = j
                        left_idx[1] = k

                    elif L1 + L2 > R1 + R2:
                        answer += 'R'
                        right_idx[0] = j
                        right_idx[1] = k
                        break

                    else: # 둘이 같은 경우
                        if hand == 'left':  # 핸드가 레프트면
                            answer += 'L'
                            left_idx[0] = j
                            left_idx[1] = k
                            break

                        else: # 핸드가 라이트면
                            answer += 'R'
                            right_idx[0] = j
                            right_idx[1] = k
                            break

    return answer

# numbers =  	[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
# hand = 'left'
# print(solution(numbers, hand))
