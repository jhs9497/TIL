N = int(input())
N_list = list(map(int, input().split()))
left = 0
right = N-1

def quick_sort(N_list, left, right):
    if left < right:
        pivot = N_list[right]
        mid = (left + right) // 2
        L = left
        R = left
        while R <= right:
            if N_list[R] < pivot:
                N_list[L], N_list[R] = N_list[R], N_list[L]
                L += 1
            R += 1

        N_list[L], N_list[R-1] = N_list[R-1], N_list[L]
        print(*N_list)

        quick_sort(N_list, left, mid-1)
        quick_sort(N_list, mid+1, right)

quick_sort(N_list, left, right)