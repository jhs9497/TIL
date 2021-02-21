# 가장 큰 놈을 기준으로 왼쪽부터 for문 돌리고 오른쪽부터 역으로 for문을 돌리자
H_list = [4, 6, 3, 10, 10, 4, 6, 8]
max_idx = 0  # 가장 큰 놈의 인덱스 구하기
max_number = 0

for i in range(len(H_list)):
    if max_number < H_list[i]:
        max_number = H_list[i]
        max_idx = i

# 가장 큰 놈의 인덱스를 기준으로 ( 가장 큰 놈이 여러개여도 상관 없음)
# 왼쪽부터 정렬시키고
for i in range(max_idx):
    if H_list[i] >= H_list[i+1]: # 만약 나보다 오른쪽 놈이 나보다 작거나 같으면
        H_list[i+1] = H_list[i]  # 그 놈을 나랑 똑같게 만든다

# 오른쪽도 정렬
for i in range(len(H_list)-1, max_idx, -1):
    if H_list[i] >= H_list[i-1]:  # 만약 나보다 왼쪽 놈이 나보다 작거나 같으면
        H_list[i-1] = H_list[i]   # 그 놈을 나랑 똑같게 만든다

print(H_list)
# 내가 원하느 답은 [3, 5, 5, 9, 7, 7, 7]





