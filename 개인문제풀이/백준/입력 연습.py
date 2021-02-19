
switch = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

answer = [[3]*20 for _ in range(5)]

A = -1
i = 0
j = -1
while A < len(switch)-1:
    A += 1
    j += 1
    answer[i][j] = switch[A]
    if j == 19:
        i += 1
        j = -1

for i in range(5):
     str_answer = ''
     for j in range(20):
         if answer[i][j] <3:

             str_answer += str(answer[i][j])
             str_answer += ' '
         else:
             break
     print(str_answer)
