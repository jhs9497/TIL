def cartesian(p, q):
    x1, y1 = findxy(p) # &p를 구하는 함수
    x2, y2 = findxy(q) # &q를 구하는 함수
    return findxy2(x1+x2, y1+y2)
 
 
def findxy(n): # ex) p가 6이면 n == 6
    result = [0, 2] # 왜 시작이 여기지 ? 대각선 방향으로 진행시키기 위함임 p가 1일 때 (1,1)이 되어야 하니깐
    cnt = 0
    while cnt < n: 
        if result[1] == 1: # y축이 1이면
            result[1] = result[0] + 1 # y축은 x축 + 1 -> 새로운 대각선의 맨 위쪽
            result[0] = 1 # x축은 1 -> 새로운 대각선의 맨 왼쪽
        else: # 그렇지 않으면
            result[0] += 1 # x축은 1씩 더해주고 
            result[1] -= 1 # y축은 1씩 빼준다..?  --> 우하향하라
        cnt += 1
    return result[0], result[1]
 
def findxy2(x, y):
    result = [0, 2]
    cnt = 0
    while result[0] != x or result[1] != y: # x,y값에 도달하기 전까지 신선한 while문이군
        if result[1] == 1: # 똑같이 진행하고
            result[1] = result[0] + 1
            result[0] = 1
        else:
            result[0] += 1
            result[1] -= 1
        cnt += 1        
    return cnt  # 카운트를 리턴한다
 
t = int(input())
for test_case in range(t):
    p, q = map(int, input().split())       
    print('#' + str(test_case + 1), cartesian(p, q)) # #1 을 더하는 새로운 방법