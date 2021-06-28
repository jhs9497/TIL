
def game(i, j):
    if i == j:
        return i
    a = game(i, (i+j)//2) -1  # why? 인덱스니깐
    b = game((i+j)//2+1, j) -1

    if arr[a] == '1': #arr[a]가 1이면
        if arr[b] == '1':


        elif arr[b] == '2':





for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    game(1, N)
    print(game(1, N))




