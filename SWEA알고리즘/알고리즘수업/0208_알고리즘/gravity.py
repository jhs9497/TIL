A = [7, 4, 2, 0, 0, 6, 0, 7, 0]

answer = 0
for i in range(len(A)-1): # 0~8 9번을 돌린다   # i = 0  7층짜리가 먼저 선정
    count = 0
    for j in range(i+1, len(A)): # i= 1부터 뒤까지 비교하려고 1~9까지 1~8번째
        if A[i] > A[j]:
            count += 1
            if answer < count:
                answer = count
print(answer)

# A = [7, 4, 2, 0, 0, 6, 0, 7, 0]
#
# Count_A = [0] * 10
#
# # Count_A = [4, 0, 1, 0, 1, 0, 1, 2, 0, 0]
#
# for i in A: # list A
#     for j in range(len(Count_A)):  # 0부터 9까지
#         if i == j:
#             Count_A[j] += 1
# print(Count_A)











