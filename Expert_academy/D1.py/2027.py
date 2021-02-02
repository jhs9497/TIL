A = '+'


numbers = [1, 7, 13, 19, 25]
result =''


for i in range(1, 26):
        if i == 
            result += '#'
        else:
            result += '+'
            
answer = ''
count = 0

for i in result:
    answer += i
    count += 1
    if count == 5:
        print(answer)
        count = 0
        answer = ''




number = -1
for re in range(0,5):
    number += 1
    result = ''
    for idx in range(0,5):

        if idx == number :
            result +='#'
        else:
            result += '+'
    print(result)