# A = chr(65)
# print(A)

# 'A'~'Z'를 뽑기 위한 아스키코드 숫자는 65~90

for tc in range(1, int(input())+1):
    # 우선 빈 문자열로 이루어진 N X N 배열을 만들자
    N = int(input())
    answer = [['']*N for _ in range(N)]
    # 열 기준 0,1,3,5, 는 아래로 향하게 2,4,6,8 은 위로 향하게 (문자사각형2처럼)
    asci = 65  # 시작점인 A를 지칭하는 asci 숫자 세팅
    count = 1 # 몇번째 시돈지 count하기 위한 용도
    M = 0 # 고정된 열을 표현
    for _ in range(N): # 세로줄로 한번씩 채워나갈 것이기 때문에 N X N 행렬에서 N번 반복해야한다
        if count % 2 == 0: # 만약 count가 홀수면 왼쪽에서 두번째 세로줄이라는 뜻이므로 아래에서 위로 인덱싱
            for j in range(N-1, -1, -1): # 문자사각형1 문제처럼 푼다
                answer[j][M] = chr(asci)  # 여기서 열은 M으로 고정되야 해서 위에 M값을 줌
                asci += 1
                if asci == 91: 
                    asci = 65   
            count += 1  # 세로 1줄이 끝나면 count와 M을 모두 1씩 증가시켜서 다음 세로줄을 표현해준다
            M += 1 
        else: # count가 홀수면
            for j in range(N): # 동일하지만 위에서 아래로 인덱싱 해야하므로 j가 0 1 2 3 4 5이렇게 나오게 해준다
                answer[j][M] = chr(asci)    
                asci += 1 
                if asci == 91: 
                    asci = 65   
            count += 1
            M += 1

    print('#{}'.format(tc)) 
    # 리스트로 된 answer를 스트링화 하자
    for a in range(len(answer)):
        real_answer = '' # 한줄 씩 뽑고 바로 초기화
        for b in range(len(answer)):
            real_answer += answer[a][b]
            real_answer += ' ' # 띄어쓰기 해주기
        print(real_answer) # 한 줄씩 answer 행렬 뽑아주기
