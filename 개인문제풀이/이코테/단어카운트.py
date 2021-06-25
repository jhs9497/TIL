input_list = ['미래', '비전', '창조', '미래', '역사']

word_list = list(set(input_list))

word_count = [0] * len(word_list)

for i in range(len(word_list)):
    for j in range(len(input_list)):
        if word_list[i] == input_list[j]:
            word_count[i] += 1

for k in range(len(word_list)):
    print(f'{word_list[k]}:{word_count[k]}')