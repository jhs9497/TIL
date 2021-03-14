for tc in range(1, int(input())+1):
    N, K = map(int, input().split()) # N X N 지도, K -> 최대 공사 가능 깊이
    MAP = [list(map(int, input().split())) for _ in range(N)]

    print(max(max(MAP)))