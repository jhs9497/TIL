answers = [1,3,2,4,2]

A = [1,2,3,4,5] # 1번 수포자의 패턴
B = [2,1,2,3,2,4,2,5] # 2번 수포자의 패턴
C = [3,3,1,1,2,2,4,4,5,5] # 3번 수포자의 패턴

answer_idx = 0 #
A_idx, B_idx, C_idx = 0, 0, 0
A_count, B_count, C_count = 0, 0, 0

while answer_idx < len(answers):
    if answers[answer_idx] == A[A_idx]: A_count += 1

    if answers[answer_idx] == B[B_idx]: B_count += 1

    if answers[answer_idx] == C[C_idx]: C_count += 1

    answer_idx += 1

    if A_idx >= len(A) -1:
        A_idx = 0
    else:
        A_idx += 1

    if B_idx >= len(B) -1:
        B_idx = 0
    else:
        B_idx += 1

    if C_idx >= len(C) -1:
        C_idx = 0
    else:
        C_idx += 1

result = []
count_list = [A_count, B_count, C_count]
max_count = max(count_list)
for i in range(len(count_list)):
    if max_count == count_list[i]:
        result.append(i+1)

print(result)

