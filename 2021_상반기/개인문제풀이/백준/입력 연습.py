
T = int(input())

for tc in range(1, T + 1):

    arr = input()
    n = len(arr)
    scd = dcd = hcd = ccd = 0
    print("#{}".format(tc), end=' ')

    # 그냥 문자로 통으로 들어오기 때문에 각각 하나의 str로 만들기 위해서 빈 리스트에 넣었고
    fst = []
    for i in range(n):
        fst.append(arr[i])
    # 012 345 678 91011 이렇게 3개씩 넣기 위해서 범위를 정해주고 변수에 +를 해줌.
    lst = []
    for i in range(n // 3):
        x = fst[i * 3] + fst[i * 3 + 1] + fst[3 * i + 2]
        lst.append(x)
    # 셋 함수를 이용해서, 중복이 제거가 되었다면, 에러를 출력하게 만들고
    if len(lst) > len(set(lst)):
        print("ERROR")
        continue      # 테스트케이스의 포문을 계속 돌려야 하니깐 에러를 출력하면서, 해당포문은 끝내고
    else:           # 다음 테스트 케이스부터 시작.

        for k in range(n // 3):
            if arr[3 * k] == "S":
                scd += 1
            elif arr[3 * k] == "D":
                dcd += 1
            elif arr[3 * k] == "H":
                hcd += 1
            elif arr[3 * k] == "C":
                ccd += 1

        s = 13 - scd
        d = 13 - dcd
        h = 13 - hcd
        c = 13 - ccd

    print("{} {} {} {}".format(s, d, h, c))
