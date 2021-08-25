n, r = input().split()
n = int(n)
r = int(r)
num_list = list(map(int, input().split()))

sel = [-1] * r
door = 'close'
answer = 'NO'

def combi(k, start):
    global door
    global answer
    if k == r:
        if door == 'open':
            answer = 'YES'
            print(*sel)
        if sel == num_list:
            door = 'open'
        else:
            door = 'close'
        
    else:
        for i in range(start, n-r+k+1):
            sel[k] = i+1
            combi(k+1, i+1)

combi(0, 0)

if answer == 'NO':
    print('NONE')