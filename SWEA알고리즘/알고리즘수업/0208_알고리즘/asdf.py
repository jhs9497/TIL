lst = [0, 0, 3, 5, 2, 4, 9, 0, 6, 4, 0, 6, 0, 0]


cnt = 0   # 최종 조망 층수 넣을 cnt 
          # 제일 바깥인 이유 : i가 지정되고 밑에 모든 구문을 한 바퀴 다 돌아야 lst[i+2] 한 건물의 조망권이 확보되기 때문
for i in range(len(lst)-2): 

    if lst[i+2] > lst[i] and lst[i+2] > lst[i+1] and lst[i+2] > lst[i+3] and lst[i+2] >lst[i+4]: 
        A = [lst[i], lst[i+1], lst[i+3], lst[i+4]]

        max_ = 0 # max_를 여기 두는 이유: 밑에 z for문이 한 바퀴 다 돌아야 양 옆 총 4개 건물중 제일 큰 놈을 알 수 있기 때문
        for z in range(len(A)):  

            if max_ < A[z]:     # 만약 A[0] 건물이 max_ 보다 크다면 
                max_ = A[z]     # max_ = A[0]
                                # 만약 A[1] 건물이 max_ 보다 크다면
                                # max_ (현재는 A[0])= A[1]
                                # 만약 A[2] 건물이 max_ 보다 작다면
                                # max_ = 그대로 A[1]
        
        cnt += lst[i+2] - max_  # 이렇게 list[i+2]의 옆 건물 중 제일 큰놈을 구하면 맨위에 cnt에다가 최종값을 넣어준다.

print(cnt)