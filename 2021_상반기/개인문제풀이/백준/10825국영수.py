# ord, chr

students_score = []
for _ in range(int(input())):
    name, K, E, M = input().split()
    students_score.append([int(K), int(E), int(M), name])

# 국어 점수 감소하는 순서대로
students_score.sort(reverse=True)

cnt = 0
# 국어 점수가 같으면 영어 점수가 증가하는 순서대로
for _ in range(len(students_score)): # 반복횟수의 이미
    for i in range(len(students_score)-1): 
        if students_score[i][0] == students_score[i+1][0] and students_score[i][1] == students_score[i+1][1] and students_score[i][2] == students_score[i+1][2]:
            cnt += 1
            # 점수가 모두 같다면
        if students_score[i][0] == students_score[i+1][0]: # 국어점수가 같으면
            if students_score[i][1] <= students_score[i+1][1]: # 뒤에 친구 영어점수가 더 높으면
                continue # 넘어가고
            else: # 뒤에 친구 영어점수가 더 낮으면
                students_score[i], students_score[i+1] = students_score[i+1], students_score[i] # 자리 바꿔주기


# 영어 점수가 같으면 수학 점수가 감소하는 순으로
for _ in range(len(students_score)): # 반복횟수의 이미
    for i in range(len(students_score)-1): 
        if students_score[i][1] == students_score[i+1][1]: # 영어점수가 같으면
            if students_score[i][2] >= students_score[i+1][2]: # 뒤에 친구 수학점수가 더 낮으면
                continue # 넘어가고
            else: # 뒤에 친구 수학점수가 더 높으면
                students_score[i], students_score[i+1] = students_score[i+1], students_score[i] # 자리 바꿔주기


# 점수가 모두 같다면 사전순으로 증가하는 순서대로
for _ in range(cnt):
    for i in range(len(students_score)-1): 
        if students_score[i][0] == students_score[i+1][0] and students_score[i][1] == students_score[i+1][1] and students_score[i][2] == students_score[i+1][2]:
            # 점수가 모두 같다면
            front = len(students_score[i][3]) # 앞친구의 이름 길이
            back = len(students_score[i+1][3]) # 뒤친구의 이름 길이
            if front < back:
                K = front # K는 이름 사전순 비교할때 쓰일 for문의 range 두친구의 이름길이 중 더 작은수로 해야함
            else:
                K = back
            
            for j in range(K):
                if ord(students_score[i][3][j]) > ord(students_score[i+1][3][j]): # 사전순으로 비교하고
                    
                    students_score[i], students_score[i+1] = students_score[i+1], students_score[i] # 자리 바꿔주기
                    break # 비교됐으면 바로 그만

                elif ord(students_score[i][3][j]) < ord(students_score[i+1][3][j]): # == 인 경우만 for j in range(K)가 진행되도록
                    break

for k in range(len(students_score)):
    print(students_score[k][3])


