def check(width, num, wrongs):
    start = wrongs[0][1]
    for idx in range(1, len(wrongs)):
        if start + width < wrongs[idx][1]:
            start = wrongs[idx][1]
            num -= 1
            if num == 0:
                return False
    else:
        return True


N, M = map(int, input().split())
num = int(input())
w = int(input())
wrongs = [list(map(int, input().split())) for _ in range(w)]
wrongs.sort(key=lambda x: x[1])

start = max([i[0] for i in wrongs])
end = max([i[1] for i in wrongs])

while start <= end:
    middle = (start + end) // 2
    if check(middle - 1, num, wrongs):
        end = middle - 1
    else:
        start = middle + 1

print(start)