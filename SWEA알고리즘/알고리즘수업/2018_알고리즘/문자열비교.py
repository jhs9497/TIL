for tc in range(1, int(input())+1):
    str1 = input()
    N = len(str1) # 움직이는 스트링
    str2 = input()
    M = len(str2)  # 기준 스트링

    # N = 4
    # M = 10 이라 가정

    answer = 0
    for i in range(M-N+1): # i = 0,1,2,3,4,5,6,7 (str2의 인덱싱)
        str1_1 = ''
        str2_2 = ''
        for j in range(N): # j = 0,1,2,3 (str1의 인덱싱)
            str1_1 += str1[j]
            str2_2 += str2[i+j]

        if str1_1 == str2_2:
            answer += 1

    if answer > 0:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))


