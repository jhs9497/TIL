arr = [1,2,3]

N = 3

sel = [0]* N # 결과들이 저장될 리스트
check = [0]* N # 해당 원소를 이미 사용했는지 안했는지에 대한 체크


def perm(idx):
    # 다 뽑아서 정리 했다면
    if idx == N:
        print(sel)
    else:
        for i in range(N):
            if check[i] == 0:  # 해당 원소는 아직 사용하지 않았다는 것!
                sel[idx] = arr[i]  # arr에 i번째 원소를 활용하지 않았다는 뜻이니깐 sel자리에 넣어!
                check[i] = 1 # check에도 사용하였음을 말해준다
                perm(idx+1) # 재귀로 +1 해서 돌리고  흠,, 돌아나오는게 뭐지 ? ?
                check[i] = 0 # check는 다시 써야하니깐 원상복구

perm(0)