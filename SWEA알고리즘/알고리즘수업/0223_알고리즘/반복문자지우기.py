
for tc in range(1, int(input())+1):
    string = input()
    i = 0
    while True:
        if i == len(string)-1:
            break
        if string[i] == string[i+1]:
            str1 = string[0:i]
            str2 = string[i+2:]
            string = str1 + str2
            i = 0
        else:
            i += 1

    print('#{} {}'.format(tc, len(string)))


