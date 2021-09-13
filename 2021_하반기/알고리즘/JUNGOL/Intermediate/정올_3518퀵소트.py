N = int(input())
N_list = list(map(int, input().split()))
left = 0
right = N-1

def quick_sort(N_list, left, right):
    if left < right:
        idx = (left + right) // 2
        # 피봇은 리스트의 가운데 친구로 잡는다. 이것이 일반적으로 가장 빠르다.
        pivot = N_list[right]
        # 피봇으로 선정한 친구와 리스트의 가장 오른쪽친구랑 자리를 바꿔준다.
        N_list[idx], N_list[right] = N_list[right], N_list[idx]

        # L, R 모두 리스트의 가장 첫 번째 인덱스로 우선 설정해준다.
        L = left
        R = left

        # R이 리스트를 넘어가기 전까지 while문
        while R <= right:
            # 만약 R인덱스의 요소가 pivot보다 작다면
            if N_list[R] < pivot:
                # L인덱스 요소와 R인덱스 요소를 바꿔주고
                N_list[L], N_list[R] = N_list[R], N_list[L]
                # R인덱스가 pivot보다 작을 때만 L 인덱스는 +1 해준다.
                L += 1
            # R인덱스는 항상 + 1 해준다.
            R += 1

        # while문 나오고 L인덱스의 위치가 파티셔닝을 할 기준이 될 인덱스다.
        p_idx = L

        # 피봇도 L인덱스의 요소와 바꿔주면서 자기 자리로 위치하게 설정해주고
        N_list[L], N_list[R-1] = N_list[R-1], N_list[L]
        print('정렬중인 list', *N_list, '파티션 기준 인덱스 =', p_idx)

        # p_idx( 과거 L )을 기준으로 왼쪽 리스트와 오른쪽 리스트를 재귀호출한다.
        quick_sort(N_list, left, p_idx-1)
        quick_sort(N_list, p_idx+1, right)

quick_sort(N_list, left, right)