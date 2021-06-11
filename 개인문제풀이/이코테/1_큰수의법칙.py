N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

# 가장 큰 2개의 수로 (중복되더라도) K만큼 반복해서 가장 큰수를 더하고 K초과 됐을 때 2번째로 큰수를 한번 더해주면된다.
# 우선 arr을 오름차순으로 정렬하고 [2, 4, 4, 5, 6] 으로 변함
arr.sort()

# first와 second에 arr 맨 뒤, 맨뒤에서 2번째 값을 넣어준다.
first = arr[-1]
second = arr[-2]

M_count = 0 # 전체 시행횟수는 M번보다 적어야함
K_count = 0 # 연속으로 더할 수 있는 횟수는 K보다 적어야함
answer = 0 # 최종 답안

# M_count가 M보다 작은 동안 While문 돌리고
while M_count < M:
    # 만약 K_count가 K보다 작으면
    if K_count < K:
        # 가장 큰 수 정답에 더해주고
        answer += first
        # K_count +1
        K_count += 1
    # K_count가 K랑 같아지면
    elif K_count == K:
        # 두번째로 큰 수 정답에 더해주고
        answer += second
        # K_count 초기화
        K_count = 0
    # if/elif와 상관없이 M_count(전체시행횟수) +1
    M_count += 1

print(answer)