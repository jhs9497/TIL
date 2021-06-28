
L_list = [2,4,5,8,9,11,13,16]
H_list = [4,6,6,10,10,8,8,8]

max_idx = 3

total = 0
for i in range(max_idx):
    total += (L_list[i+1]-L_list[i]) * H_list[i]  # 인접한 L의 차 X 그에 맞는 H를 total에 더해주는 것이다.


# 뒤에서 ~ max_idx까지
for i in range(len(H_list)-1, max_idx, -1):
    total += (L_list[i]-L_list[i-1]) * H_list[i]
    print(i)
    print(total)

# 마지막으로 기준이 되는 max_idx 값 total에 추가
total += H_list[max_idx]
print(total)

