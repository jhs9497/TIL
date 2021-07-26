def bingo_check(bingo_board, bingo_number):

    count = 0
    for i in range(5):
        for j in range(5):

            now_number = bingo_number[i][j]

            for a in range(len(bingo_board)):
                for b in range(len(bingo_board)):
                    if now_number == bingo_board[a][b]:
                        bingo_board[a][b] = 0
                        count += 1
                        break

            if count > 11:
                bingo = 0
                # 가로줄 체크
                for x in range(5):
                    is_bingo = 0
                    for y in range(5):
                        if bingo_board[x][y] == 0:
                            is_bingo += 1

                    if is_bingo == 5:
                        bingo += 1
                # 세로줄 체크
                for q in range(5):
                    is_bingo = 0
                    for w in range(5):
                        if bingo_board[w][q] == 0:
                            is_bingo += 1

                    if is_bingo == 5:
                        bingo += 1

                # 우하향 대각선 체크
                is_bingo_right_down = 0
                for k in range(5):
                    if bingo_board[k][k] == 0:
                        is_bingo_right_down += 1

                if is_bingo_right_down == 5:
                    bingo += 1

                # 우상향 대각선 체크
                is_bingo_right_up = 0
                for p in range(5):
                    if bingo_board[4-p][p] == 0:
                        is_bingo_right_up += 1
                if is_bingo_right_up == 5:
                    bingo += 1

                if bingo >= 3:
                    return count


bingo_board = [list(map(int, input().split())) for _ in range(5)]
bingo_number = [list(map(int, input().split())) for _ in range(5)]

answer = bingo_check(bingo_board, bingo_number)

print(answer)

