def solution(distance, rocks, n):
    left, right = 0, distance
    rocks.sort()
    rocks.append(distance)
    answer = 0
    while left <= right:
        prev = 0
        mins = 1e9
        removed_rocks = 0

        mid = (left + right) // 2
        for i in range(len(rocks)):
            if rocks[i] - prev < mid:
                removed_rocks += 1
            else:
                mins = min(mins, rocks[i] - prev)
                prev = rocks[i]

        if removed_rocks > n:
            right = mid - 1

        else:
            answer = mins
            left = mid + 1
    return answer

distance = 25
rocks = [2, 14, 11, 21, 17]

n = 2
solution(distance, rocks, n)