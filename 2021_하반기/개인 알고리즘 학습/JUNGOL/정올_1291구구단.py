def solution(s, e):
    number_list = []

    if 2 <= s <= 9 and 2 <= e <= 9:
        if s <= e:
            while s <= e:
                number_list.append(s)
                s += 1

        else:
            while s >= e:
                number_list.append(s)
                s -= 1

        for i in range(1, 10):
            for j in number_list:
                if i*j < 10:
                    print(f'{j} * {i} =  {j * i}', end='   ')
                else:
                    print(f'{j} * {i} = {j*i}', end='   ')
            print()

    else:
        print('INPUT ERROR!')
        s, e = map(int, input().split())
        solution(s, e)

s, e = map(int, input().split())
solution(s, e)