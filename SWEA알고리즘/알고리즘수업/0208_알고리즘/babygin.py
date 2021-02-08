
number = list(map(int, input().split()))

count_number = [0]*10

for i in number:
    for j in range(10):
        if i == j:
            count_number[j] += 1

# print(count_number)

# 같은 수 3개가 있는지 찾는 공식
count = 0
for x in count_number:
    if x >= 3:
        for z in range(len(count_number)):
            if x == count_number[z]:
                count_number[z] -= 3  # -3을 해주는 이유 : 연속 3개인 수와 겹칠 수 있음 ex) 5 5 5 4 6 7
    else:
        count += 1
if count == 10:
    print("babygin 아니요!!!!!")

else:
    # 연속 3개인 수가 있는지 찾는 공식  count_number = [0, 0, 1, 1, 1, 0, 3, 0, 0, 0]
    for y in range(len(count_number) - 2):  # y가 0부터 7까지 돌아다녀야 함 why? 밑에 y+2가 있으니깐
        # count_number[y]가 1보다는 커야함 why? 그러지 않으면 [0,0, 1, 1, 0, 0, 0, 0, 0, 1] 일 때 0도 아래 공식에 부합함
        if count_number[y] >= 1 and count_number[y] == count_number[y + 1] and count_number[y] == count_number[y + 2]:
            print("babygin 맞음! 야호")
            break
    else:
        print("babygin 아님!")
