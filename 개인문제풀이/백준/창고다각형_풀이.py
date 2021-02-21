# 우선 1000 X 1000 배열 도화지를 만들자
coordi = [[0] * 1000 for _ in range(1000)]
# 굳이 따지면 문제의 그림을 거꾸로 매달아 보는 셈인데 이 coordi는  H값을 옳바르게 정렬시키는데 사용된다

N = int(input())  # 기둥의 갯수
L_list = []  # L의 list
for _ in range(N):
    L, H = map(int, input().split())  # L과 H가 L기준 왼쪽부터 순서대로 나오는게 아니라 랜덤하게 입력된다..
    L_list.append(L)  # 우선 L은 리스트로 만들어주고
    # L을 왼쪽면에 위치라고 생각하지말고 코딩상에서 그 기둥의 인덱스라고 생각하자
    H -= 1
    # 그리고 H는 -1 해주자 why? 예를 들어 L=2, H=4 라면
    # 0,0 부터 시작하는 1000X1000 도화지에서는 0,2 1,2 2,2 3,2 4,2로 면적이 5라 측정되기 때문이다
    for i in range(H + 1):  # 레인지니깐 +1
        coordi[i][L] = 1  # 도화지에 색칠 / L은 고정시키고 H만 움직인다

# 색칠한 도화지를 이용해서 입력받은 L, H값을 L이 작은수부터 정렬되게 만들고 그와 짝인 H값도 순서대로 만들어줘야 한다.
L_list.sort()  # L_list는 sort로 작은수부터 해서 정렬

H_list = [0] * N  # H의 리스트

A = 0  # H_list에 인덱스
B = 0  # 열 검색할때 시작점
k = 0  # 각 기둥의 높이 표현
# 시작이 -1인 이유: 현재 색칠된 도화지를 돌며 k를 탐색할껀데 k=0부터 시작하면
# 0부터 센 높이의 값이 아니라 실제 높이가 나오기 때문
while A < N:  # 열검색, A가 H_list 보다 작은 동안 ( 밑에서 기둥이 발견되면 +1 씩 해줄거임 )
    for i in range(B, 1000):  # 기둥이 발견되면 그 뒤부터 검색해야하니 범위를 B로 설정 우선은 0
        k = 0  # 기둥이 발견되도 다시 돌릴 때는 초기화 해야 하므로 k = 0
        for j in range(1000):
            if coordi[j][i] == 1:  # 만약 1000 X 1000 도화지에서 coordi[1][0], [2][0], [3][0] 이렇게 돌다가 1이 발견되면
                k += 1  # k는 층수의 높이므로 +1을 해준다
        # 세로줄 한줄의 탐색이 끝났을때
        if k > 0:  # 만약 k가 발견되어 있으면
            H_list[A] = k  # H_list에 추가해주고
            A += 1  # A는 다음 인덱스를 찾아야하니 +1 해주고
            B = i + 1  # B 역시 이 다음 열부터 찾아야 하니 i+1로 입력해준다
            break

# 내가 원하는 답은 test_case라고 했을 때  // L = [2, 4, 5, 8, 11, 13, 15], H = [4, 6, 3, 10, 4, 6, 8]  잘나옴!
# 여기 까지 1000 X 1000 0의 도화지에 L,H에 맞춰서 1로 색칠했고 L,H를 리스트로 따로 빼뒀음

# 가장 큰 놈을 기준으로 왼쪽부터 for문 돌리고 오른쪽부터 역으로 for문을 돌리자
max_idx = 0  # 가장 큰 놈의 인덱스 구하기
max_number = 0

for i in range(len(H_list)):
    if max_number < H_list[i]:
        max_number = H_list[i]
        max_idx = i

# 가장 큰 놈의 인덱스를 기준으로 ( 가장 큰 놈이 여러개여도 상관 없음)
# 왼쪽부터 정렬시키고
for i in range(max_idx):
    if H_list[i] >= H_list[i + 1]:  # 만약 나보다 오른쪽 놈이 나보다 작거나 같으면
        H_list[i + 1] = H_list[i]  # 그 놈을 나랑 똑같게 만든다

# 오른쪽도 정렬
for i in range(len(H_list) - 1, max_idx, -1):
    if H_list[i] >= H_list[i - 1]:  # 만약 나보다 왼쪽 놈이 나보다 작거나 같으면
        H_list[i - 1] = H_list[i]  # 그 놈을 나랑 똑같게 만든다

# 여기까지 test_case로 치면 L = [2, 4, 5, 8, 11, 13, 15] H = [4, 6, 6, 10, 8, 8, 8] 까지 완성시켰다

# 이제 이 두 리스트를 이용하여 면적값만 구하면 된다

# 마찬가지로 제일 높은 층수의 max_idx를 기준으로 삼고
# 0~ max_idx까지
total = 0
for i in range(max_idx):
    total += (L_list[i+1]-L_list[i]) * H_list[i]  # 인접한 L의 차 X 그에 맞는 H를 total에 더해주는 것이다.

# 뒤에서 ~ max_idx까지
for i in range(len(H_list)-1, max_idx, -1):
    total += (L_list[i]-L_list[i-1]) * H_list[i]

# 마지막으로 기준이 되는 max_idx 값 total에 추가
total += H_list[max_idx]

print(total)

