N = int(input())
arr = list(map(int, input().split()))
con = 0  # 현재 상태를 의미 시작은 0 수열의 초반부분을 보고 결정
Max_count = 1
count = 1 # 디폴트 값은 1이어야함 why? 지금 arr[i] 와 arr[i+1]의 관계를 보며 카운팅을 하고 있는데 정답은 원소의 갯수를 묻는 것이므로

# for i in range(len(arr)-1): # 수열을 돌면서
#     if arr[i] > arr[i+1]:  # 만약 왼쪽 값이 더 크다면
#         con = -1 # 수열중 가장 먼저 변화되는 부분은 작아지고 있다는 의미에서 -1
#         break  # con의 초기값만 필요했으므로 break
#
#     elif arr[i] < arr[i+1]:
#         con = 1  # 커지고 있는 상태라는 의미로 1
#         break
#     else:
#         continue

for i in range(len(arr)-1): # 다시 수열을 돌면서
    if arr[i] > arr[i+1]: # 만약 왼쪽 값이 더 크다면
        if con == -1 or con == 0: # 수열이 현재 작아지고 있는 상황이면
            count += 1
        else: # 커지고 있는 상황이면
            count = 1 # count 초기화
        con = -1  # 상태 표시

    elif arr[i] < arr[i+1] : # 반대도 똑같이
        if con == 1 or con == 0:
            count += 1
        else:
            count = 1
        con = 1 # 상태 표시

    else: # arr[i] == arr[i+1]의 경우는 어떤 경우던 count 추가이니
        count += 1


    if Max_count < count :  # 한 번의 확인이 끝난후에 현재의 count값을 기준으로 가장 큰 count 골라내기
        Max_count = count

print(Max_count)