New_number = []
numbers = [6, 1003, 212, 2225]
answer = ''

for i in numbers:
    if i < 10:
        New_number += [[i]]  # 10보다 작으면 그냥 추가

    else:  # 그렇지 않으면 while문으로 새로운 리스트 만들어서 추가
        str_list = []
        while i // 10 > 0:
            str_list.append(i%10)
            i = i // 10
        str_list.append(i) # 마지막에 맨 앞자리수 더해주고
        str_list.reverse()  # 거꾸로 쌓여있을테니 돌려주기
        New_number += [str_list]


for i in range(len(New_number)):







