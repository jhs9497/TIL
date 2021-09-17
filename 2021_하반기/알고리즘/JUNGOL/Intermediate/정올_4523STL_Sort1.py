import copy

N = int(input())
N_list = list(map(int, input().split()))
s, e = map(int, input().split())

copy_list = copy.deepcopy(N_list)
slice_sort = copy_list[s:e+1]
slice_sort.sort()

j = 0
for i in range(s, e+1):
    copy_list[i] = slice_sort[j]
    j += 1

N_list.sort()

print(*copy_list)
print(*N_list)