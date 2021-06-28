N = int(input())  # 기둥의 숫자

my_dict = {} # 우선 x,h를 딕트로 받고
x_list = [] # x는 x_list에도 받으면서 나중에 sort
h_list = [] # sort한 x_list를 이용해서
for i in range(N):
    x, h = map(int, input().split())
    my_dict[x] = h  # x : h로 딕트만들고
    x_list.append(x)
    x_list.sort()  # x_list는 따로 만든 다음 sort해준다

for x in x_list:  # sort된 x_list를 돌면서
    h_list.append(my_dict[x]) # 정렬된 x값에 상응하는 h값을 x의 순서대로 h_list에 추가해준다

# 여기까지 x,h를 정렬해서 2개의 리스트로 만들었다.

M = max(h_list)  # 기둥들 중 가장 높은 기둥 찾고
max_idx = 0  # 그 기둥의 인덱스를 찾는다

for i in range(len(h_list)):
    if M == h_list[i]:
        max_idx = i
        break

# 그 기둥을 기준으로 왼쪽 오른쪽으로 나눠서 h_list값을 조절해 줄 것이다.

for i in range(max_idx):
    if h_list[i] >= h_list[i+1]: # 만약 나보다 오른쪽 놈이 나보다 작거나 같으면
        h_list[i+1] = h_list[i]  # 그 놈을 나랑 똑같게 만든다

# 오른쪽도 정렬
for i in range(len(h_list)-1, max_idx, -1):
    if h_list[i] >= h_list[i-1]:  # 만약 나보다 왼쪽 놈이 나보다 작거나 같으면
        h_list[i-1] = h_list[i]   # 그 놈을 나랑 똑같게 만든다

# 여기까지 x, h를 정렬, 컨트롤했다.
# 예시로 치면 x_list = [2,4,5,8,11,13,15] h_list = [4,6,6,10,8,8,8]

# 이제 이 두 리스트를 이용하여 면적값만 구하면 된다

# 마찬가지로 제일 높은 층수의 max_idx를 기준으로 삼고
# 0~ max_idx까지
total = 0
for i in range(max_idx):
    total += (x_list[i + 1] - x_list[i]) * h_list[i]  # 인접한 L의 차 X 그에 맞는 H를 total에 더해주는 것이다.

# 뒤에서 ~ max_idx까지
for i in range(len(h_list) - 1, max_idx, -1):  #6 5 4
    total += (x_list[i] - x_list[i - 1]) * h_list[i]

# 마지막으로 기준이 되는 max_idx 값 total에 추가
total += h_list[max_idx]

print(total)
