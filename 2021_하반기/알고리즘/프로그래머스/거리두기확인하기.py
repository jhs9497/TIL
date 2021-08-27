def solution(places):
    answer = []
    N = len(places)

    for i in range(N):
        place = places[i]
        place_result = check(place)
        answer.append(place_result)

    return answer


def check(place):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for x in range(len(place)):
        for y in range(len(place[0])):
            if place[x][y] == 'P':
                for i in range(4):
                    new_x = x + dx[i]
                    new_y = y + dy[i]
                    if 0 <= new_x < len(place) and 0 <= new_y < len(place[0]):
                        if place[new_x][new_y] == 'P':
                            return 0
                        elif place[new_x][new_y] == 'O':
                            P_count = 0
                            for j in range(4):
                                check_x = new_x + dx[j]
                                check_y = new_y + dy[j]
                                if 0 <= check_x < len(place) and 0 <= check_y < len(place[0]):
                                    if place[check_x][check_y] == 'P':
                                        P_count += 1

                            if P_count > 1:
                                return 0
    return 1