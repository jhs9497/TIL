N = int(input())

count = 0 # 가장 큰 수만을 남겨두아 나중에 출력
answer = [] # 우선은 리스트로 answer가 되는 수를 뽑아보자
for second in range(1, N+1): # 처음에 range(N)으로 했다가 N이 1일때 예외사항이 나와서 계속 틀림  
    reserve_count = 0 # 최종 카운트로 가기전 후보군들
    third = N - second # 3번째로 오는 수
    first = N # 첫번째로 오는 수
    reserve_answer = [first, second, third]
    while third >= 0:
        third = second-third
        second = first-second # 다음 회차에 second이기 때문에 f-s 가 가능
        first = second+third # 위에 두 계산으로 변화된 second, thrid이기에 가능
        reserve_count += 1
        reserve_answer += [third]
    
    if count < reserve_count: # 최대값의 count를 구하며 answer에도 그 값들을 담기위함
        count = reserve_count
        answer = reserve_answer

answer_ = ''  # 스트링화해서 뽑아야 하므로 answer리스트를 스트링화
for a in range(len(answer)-1):
    answer_ += str(answer[a]) + ' '

print(count+2)
print(answer_)