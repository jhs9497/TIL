N = int(input())
upper_list = []
lower_list = []
for i in range(1, N+1):
    upper_list.append(i)
    lower_list.append(int(input()))

graph = [[] for _ in range(N+1)]

for i in range(N):
    graph[lower_list[i]].append(upper_list[i])

def check(n):
    print(n, '시작점')
    global end
    global visited
    visited[n] = True
    flag = 'open'
    for node in graph[n]:
        if visited[node] == False:
            visited[node] = True
            flag = 'close'
            check(node)

    if flag == 'open':
        end.append(n)
        visited[node] = False
        print(node, '끝점')


visited = [False]*(N+1)
answer = set()
# for i in range(1, N+1):
#     start = i
#     end = []
#     check(i)
#     print(end)
end = []
check(1)