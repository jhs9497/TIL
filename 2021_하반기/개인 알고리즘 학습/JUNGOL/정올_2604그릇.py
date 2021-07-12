dish = input()

count = 10 # 맨 바닥에 있는 그릇 초기값으로 설정
for i in range(len(dish)-1):
    if dish[i] == dish[i+1]:
        count += 5
    else:
        count += 10

print(count)