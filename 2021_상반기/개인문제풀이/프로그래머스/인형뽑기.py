board =  [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]


def solution(board, moves):
    stack = []
    count = 0
    for i in moves:
        for j in range(len(board[0])):
            if board[j][i-1] != 0:  # 인형을 뽑을 수 있는데
                if len(stack) < 1: # 비어 있으면 그냥 넣고
                    stack.append(board[j][i-1])
                    board[j][i-1] = 0 # 뽑은 인형 없애고
                    break

                elif len(stack) > 0 and stack[-1] == board[j][i-1]:
                    # 만약 스택이 차있으면서 스택의 맨위랑 지금 집은 인형이랑 같으면
                    stack.pop()  # 맨 위 인형 팝하고
                    board[j][i-1] = 0 # 뽑은 인형 없애고
                    count += 2 # 한번 pop할때 마다 인형 2개씩 사라지는 거니깐 count에 + 2
                    break

                else:
                    stack.append(board[j][i-1])
                    board[j][i-1] = 0
                    break
    return count


