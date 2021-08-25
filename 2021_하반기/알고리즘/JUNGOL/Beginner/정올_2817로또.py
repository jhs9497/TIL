number_list = list(map(int, input().split()))
n = number_list[0]
number_list.pop(0)
r = 6
sel = [0]*r

def combi(k, start):
    if k == 6:
        print(*sel)
    else:
        for i in range(start, n-r+k+1):
            sel[k] = number_list[i]
            combi(k+1, i+1)

combi(0,0)