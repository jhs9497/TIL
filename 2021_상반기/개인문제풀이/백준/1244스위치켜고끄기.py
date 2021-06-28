X = int(input())

switch = list(map(int, input().split()))

for tc in range(1, int(input())+1):
    S, N = map(int, input().split())

    if S == 1:  # 만약 성별이 남자라면
        for i in range(1, len(switch)+1): # for문을 돌리면서 스위치 번호가 1~N이니 1부터 세주고
            if i % N == 0: # i가 N의 배수라면
                if switch[i-1] == 0: # 인덱싱으론 i-1 해주고 1 이면 0으로, 0이면 1로 바꿔준다
                    switch[i-1] = 1
                else:
                    switch[i-1] = 0

    else:
        N -= 1 # 받을 N을 우리가 편한 인덱스로 바꿔주고
        start = N - 1  # 비교 시작점
        end = N + 1  # 비교 끝점
        stop = 0 # while문 끝내는 트리거
        while start >= 0 and end <= X and stop == 0:
            start -= 1 # 한칸 왼쪽으로 일단 가고!
            end += 1 # 한칸 오른쪽으로
            if switch[start] != switch[end] or start <= 0 or end > X:  # 틀리거나 벗어나면
                stop = 1  # 스탑!
            else: # 맞으면
                stop = 0 # 진행
        # start점과 end점을 알았으니 이것을 for문으로 돌리며 바꿔주면됨

        for x in range(start, end+1):
            if switch[x] == 0:
                switch[x] = 1
            else:
                switch[x] = 0

# 마지막에 문제에 맞게 스트링화

switch_ = ''
for i in range(X):
    switch_ += str(switch[i])
    switch_ += ' '

print(switch_)

# 출력 스타일에 맞추기가 실패한건가

# answer = [[3]*20 for _ in range(5)]
#
# A = -1
# i = 0
# j = -1
# while A < len(switch)-1:
#     A += 1
#     j += 1
#     answer[i][j] = switch[A]
#     if j == 19:
#         i += 1
#         j = -1
#
# for i in range(5):
#      str_answer = ''
#      for j in range(20):
#          if answer[i][j] <3:
#
#              str_answer += str(answer[i][j])
#              str_answer += ' '
#          else:
#              break
#      if str_answer == '':
#          break
#      else:
#          print(str_answer)


