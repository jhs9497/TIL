# 5개 중에 3개씩 뽑아보자 5C3  => nCr
# 0, 1, 2 # 1, 2, 3
# 0, 1, 3 # 1, 2, 4
# 0, 1, 4 # 1, 3, 4
# 0, 2, 3 # 2, 3, 4
# 0, 2, 4
# 0, 3, 4

# K : 0 -> 2까지 반복 : sel[0] 자리엔 0~2가 올 수 있고
# K : 1 -> 3까지 반복 : sel[1] 자리엔 1~3이 올 수 있고
# K : 2 -> 4까지 반복 : sel[2] 자리엔 2~4가 올 수 있다

def comb(k, s):
    if k == r:
        print(sel)
        return
    else:
        for i in range(s, n-r+k+1):
            sel[k] = i
            print(sel)
            comb(k+1, i+1)
n = 5
r = 3
sel = [-1] * 3
comb(0, 0)