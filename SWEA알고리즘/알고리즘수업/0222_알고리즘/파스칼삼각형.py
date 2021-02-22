# 파스칼 삼각형의 첫번째, 마지막번째 수는 무조건 1! 즉 인덱스가 0이거나 len(행)이면 1!
for tc in range(1, int(input())+1):
    print('#{}'.format(tc))
    N = int(input())
    p_list = [0] * N # 다음 리스트를 만들때 기준이 되도록 N길이 만큼 만든다
    for i in range(1, N+1): # 행 수 만큼 층이 있으니깐
        ans = [0] * i # 우선 매 for문마다 리셋하고 프린트할 빈 리스트를 만들고
        for j in range(i): # i를 기준으로 한 행씩 파스칼 삼각형을 그려나가 보자
            if j == 0 or j == len(ans)-1 : # 만약 j가 i행에서 첫번째거나 마지막 인덱스면
                ans[j] = 1 # 1을 넣어준다
                p_list[j] = 1 # p_list에도 같은 값을 넣어준다
            else: # 아니라면
                ans[j] = p_list[j-1] + p_list[j] # 이전 행의 두 인덱스 합으로 구한다

        for k in range(i):
            p_list[k] = ans[k] # 다음 i행 값을 구할때 지금의 i행 리스트가 기준이 되야하므로 p_list에
                               # 현재 ans를 넣어준다

        print(*ans)