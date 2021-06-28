for tc in range(1, int(input())+1):
    num, N = input().split()
    N = int(N)
    
    print('#{}'.format(tc))

    int_list = ['ZRO','ONE','TWO',"THR","FOR","FIV",'SIX',"SVN",'EGT','NIN']

    # 문자열을 리스트로 받자
    ailen_number = list(map(str, input().split()))

    # 이 문자열을 숫자열로 바꿔주자
    earth_number = []
    for i in ailen_number:
        for j in range(len(int_list)):
            if i == int_list[j]:
                earth_number += [j]

    # 바뀐 숫자열 버블정렬
    for a in range(N-1):
        for b in range(N-1):
            if earth_number[b] > earth_number[b+1]:
                earth_number[b], earth_number[b+1] = earth_number[b+1], earth_number[b]
    
    # 맨 처음 했던것의 반대로 이번엔 숫자열을 문자열로
    answer = ''
    for a in earth_number:
        for b in range(len(int_list)):
            if a == b:
                answer += int_list[b]
                answer += ' ' # 공백추가

    print(answer)

        



