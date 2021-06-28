for tc in range(1, int(input())+1):
    Day, Month, Three_M, Year = map(int, input().split())  # 각 기간별 요금
    plan = list(map(int, input().split())) # 1년 계획

    # 달별로 Day와 Month를 비교한다.
    Plan_A = []
    for i in range(len(plan)):
        if plan[i] * Day < Month: # 만약 일별요금이 1달치보다 싸다면
            Plan_A.append(plan[i] * Day)
        else: # 반대면
            Plan_A.append(Month)

    
    # 3개월 단위와 Plan_A를 비교한다.
    # 3개월권이 이득인 구간을 찾아낸다.
    month_idx = []
    for i in range(len(Plan_A)):
        if i == 10: # 만약 11월이면
            if Plan_A[i] + Plan_A[i+1] > Three_M:
                month_idx.append([i,i+1])
        
        elif i == 11: # 만약 12월이면
            if Plan_A[i] > Three_M:
                month_idx.append([i])

        else: # 나머지경우엔
            if Plan_A[i] + Plan_A[i+1] + Plan_A[i+2] > Three_M:
                month_idx.append([i,i+1,i+2])
        
    print(month_idx)

    answer = 999999999
    for i in range(len(month_idx)):
        visited = [False] * len(month_idx)
        visited[i] = True # 방문쳌,,,
        for j in range(len(month_idx)): # 비교대상이 되는 구간
            cnt = 1 # 하나의 구간을 pick하고 시작하니깐 초기값은 1
            answer_idx = month_idx[i]
            for k in month_idx[i]:
                if k in month_idx[j]: # 하나라도 겹치는 구간이 있으면
                    break # 스탑
                
                elif visited[j] == False: # 겹치는 구간도 없고 아직 방문전이면
                    cnt += 1 # cnt추가해주고
                    answer_idx += month_idx[j]
                
                # 한 경우의 구간합(?) 구한 후
                potential = cnt * Three_M # 우선 3개월권 추가된 횟수만큼이 초기값
                for a in range(len(Plan_A)): # Plan_A를 돌면서
                    if a not in answer_idx: # 만약 answer_idx에 없으면
                        potential += Plan_A[a] # 추가

                # 후보가 되는 답 구한후
                if answer > potential:
                    answer = potential # 최소값으로 갱신

                
    # 마지막으로 1년이용권과 비교해준다.
    if answer == 999999999: # 3개월권이 사용되지 않았다면
        if sum(Plan_A) < Year:
            print('#{} {}'.format(tc, sum(Plan_A)))

        else:
            print('#{} {}'.format(tc, Year))

    else:
        if answer < Year:
            print('#{} {}'.format(tc, answer))

        else:
            print('#{} {}'.format(tc, Year))
        

    