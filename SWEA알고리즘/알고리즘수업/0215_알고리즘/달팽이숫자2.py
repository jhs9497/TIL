N = 5

snail = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

for i in range(1, N +1):

    snail[0][i-1] = i  # 1~5까지는 해결


# 44332211

play_list = [] # 횟수 리스트

for j in range(N-1, 0, -1):
    play_list += [j]

 number = N
for a in play_list:   #4321
    if a % 2 == 0:

        # 아래로 a번







