for _ in range(int(input())):
    N = int(input())
    cloth_dict = {}
    cloth_list = []
    for _ in range(N):
        A, B = input().split()
        cloth_list.append((A, B))

    cloth_list = set(cloth_list)
    cloth_list = list(cloth_list)
    
    for i in range(len(cloth_list)):
        if cloth_list[i][1] in cloth_dict:
            cloth_dict[cloth_list[i][1]] += 1
        else:
            cloth_dict[cloth_list[i][1]] = 2

    answer = 1
    for count in cloth_dict.values():
        answer *= count

    answer -= 1

    print(answer)

