# n = [1, 2, 2, 2, 2, 3, 3, 3, 4, 5,            6, 1, 2, 3]
#
# cnt = [0] * 10  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#                 # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in n:  # 1부터 해서 2 2 2
#     for j in range(len(cnt)): # 0부터 9
#         if i == j:
#             cnt[j] += 1
# print(cnt)


A = [7, 3, 2, 0, 0, 6, 0, 7, 0]

result = 0  # 최종 답안이 가능한 숫자 cnt 중에 제일 큰놈
for i in A: # cnt 4 뭐 이러면
    cnt = 0
    for k in range(len(A)):
        if i > A[k]:
            cnt += 1
    if result < cnt:
        result = cnt

print(result)


