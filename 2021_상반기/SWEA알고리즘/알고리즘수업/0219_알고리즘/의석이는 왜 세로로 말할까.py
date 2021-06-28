for tc in range(1, int(input())+1):
    word = [input() for _ in range(5)] # 의석이가 말한거 받고

    # 의석이 칠판 그려주기
    board = [['']*15 for _ in range(5)]

    # 의석이가 5줄을 쓸 때 한 줄마다 몇 개씩 썼는지 세보자
    count = [0]*5
    for i in range(5):
        count[i] = len(word[i])

    for i in range(5):  # 5줄과
        for k in range(count[i]): # 의석이가 각 줄마다 쓴 글자수로 for문 돌며
            # 이게 되네...? range 안을 i로 변수활용하기
            board[i][k] = word[i][k]

    # 의석이 글씨로 가득한 보드 완성
    # 이제 세로로 추가하는데 빈 스트링이면 추가 X
    answer_str = ''
    for a in range(15):
        for b in range(5): # 글씨 적힌 보드 세로탐색
            if board[b][a]:   # 글씨가 뭐라도 있으면
                answer_str += board[b][a] # answer_str에 추가해라
            else:
                continue

    print('#{} {}'.format(tc, answer_str))





