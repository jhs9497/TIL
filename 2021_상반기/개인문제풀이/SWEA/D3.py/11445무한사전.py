def check(p,q):
    if p <= q: # 길이가 더 적은 놈까지 돌면서
        for i in range(p):
            if ord(P[i]) != ord(Q[i]): # 한 번이라도 둘의 문자가 다르면
                return('Y')

    else:
        for i in range(q):
            if ord(P[i]) != ord(Q[i]): # 한 번이라도 둘의 문자가 다르면 근데 ord를 뭐더러했지 ?
                return('Y')
    
    if q-p == 1 and Q[-1] == 'a':
        return 'N' 
    return 'Y' 

for tc in range(1, int(input())+1):
    P = input().rstrip()
    Q = input().rstrip()
    p = len(P)
    q = len(Q)
    
    print('#{} {}'.format(tc, check(p,q)))


