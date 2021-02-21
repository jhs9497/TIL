import sys
input = sys.stdin.readline

coordi = [[0] * 1000 for _ in range(1000)]

N = int(input())
L_list = []
for _ in range(N):
    L, H = map(int, input().split())
    L_list.append(L)
    H -= 1
    for i in range(H + 1):
        coordi[i][L] = 1

L_list.sort()

H_list = [0] * N

A = 0
B = 0
k = 0

while A < N:
    for i in range(B, 1000):
        k = 0
        for j in range(1000):
            if coordi[j][i] == 1:
                k += 1
        if k > 0:
            H_list[A] = k
            A += 1
            B = i + 1
            break

max_idx = 0
max_number = 0

for i in range(len(H_list)):
    if max_number < H_list[i]:
        max_number = H_list[i]
        max_idx = i

for i in range(max_idx):
    if H_list[i] >= H_list[i + 1]:
        H_list[i + 1] = H_list[i]


for i in range(len(H_list) - 1, max_idx, -1):
    if H_list[i] >= H_list[i - 1]:
        H_list[i - 1] = H_list[i]


total = 0
for i in range(max_idx):
    total += (L_list[i+1]-L_list[i]) * H_list[i]


for i in range(len(H_list)-1, max_idx, -1):
    total += (L_list[i]-L_list[i-1]) * H_list[i]


total += H_list[max_idx]

print(total)