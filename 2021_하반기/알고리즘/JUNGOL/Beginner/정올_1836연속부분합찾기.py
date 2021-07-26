# max_number = 0
# for i in range(N):
#     for j in range(i, N):
#         subset_number = 0
#         for k in range(i, j+1):
#             subset_number += number_list[k]
#
#         if max_number < subset_number:
#             max_number = subset_number
#
# print(max_number)

# N = int(input())
# number_list = list(map(int, input().split()))
#
# start = 0
# end = 0
#
# max_number = 0
# while start < N:
#     subset_number = 0
#     for i in range(start, end):
#         subset_number += number_list[i]
#
#     if max_number < subset_number:
#         max_number = subset_number
#
#     end += 1
#     if end == N+1:
#         start += 1
#         end = start
#
# print(max_number)

N = int(input())
number_list = list(map(int, input().split()))

start = 0
end = 0

max_number = 0
while start < N:
    subset_number = 0
    for i in range(start, end+1):
        if subset_number + number_list[i] >= subset_number:
            subset_number += number_list[i]
        else:
            break

    if max_number < subset_number:
        max_number = subset_number

    end += 1
    if end == N:
        start += 1
        end = start

print(max_number)

# 최선의 수. 각자리의 최선의 수 

