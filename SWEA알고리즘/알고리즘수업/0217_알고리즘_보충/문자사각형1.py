# A = chr(65)
# print(A)

# 'A'~'Z'를 뽑기 위한 아스키코드 숫자는 65~90

for tc in range(1, int(input())+1):
    # 우선 빈 문자열로 이루어진 N X N 배열을 만들자
    N = int(input())
    answer = [['']*N for _ in range(N)]
    # 행렬의 오른쪽 맨아래부터 위로, 오른쪽부터 왼쪽으로 움직이며 빈 스트링을 채운다.
    # N = 3 이라면 행 렬 모두 2,1,0 순으로 출력되며 인덱싱 해야한다
    asci = 65  # 시작점인 A를 지칭하는 asci 숫자 세팅
    for i in range(N-1, -1, -1): # 2, 1, 0
        for j in range(N-1, -1, -1): # 2, 1, 0
            # 열을 고정시켜야 하므로 i를 뒤로로
            answer[j][i] = chr(asci)  # -> 문자열 'A'를 뜻함
            asci += 1 # ABCDEF로 움직여야 하니깐 1 추가
            if asci == 91:  # 위에 1더하는 것 까지 합쳐서 만약 asci가 90
                asci = 65   # 즉 Z를 뽑는 숫자까지 온다면 65로 초기화하며 다시 A부터 뽑히도록 
    print('#{}'.format(tc))  # 넘버 먼저 뽑고

    # 리스트로 된 answer를 스트링화 하자
    for a in range(len(answer)):
        real_answer = '' # 한줄 씩 뽑고 바로 초기화
        for b in range(len(answer)):
            real_answer += answer[a][b]
            real_answer += ' ' # 띄어쓰기 해주기
        print(real_answer) # 한 줄씩 answer 행렬 뽑아주기



