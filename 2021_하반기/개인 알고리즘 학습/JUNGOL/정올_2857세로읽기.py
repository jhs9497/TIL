word_list = []
max_length = 0
for _ in range(5):
    input_list = list(input())
    word_list.append(input_list)
    if max_length < len(input_list):
        max_length = len(input_list)

for i in range(5):
    count = max_length - len(word_list[i])
    if count > 0:
        while count > 0:
            word_list[i].append('')
            count -= 1


answer = ''

for i in range(len(word_list[0])):
    for j in range(5):
        if word_list[j][i] == '':
            pass
        else:
            answer += str(word_list[j][i])

print(answer)
