t = int(input())
for tc in range(1, t+1):
    x = input()
    abc = list(x)
    n = len(abc)
    N = 100
    while N > 0:
        for i in range(n-1):
            if abc[i] == abc[i+1]:
                abc[i] = abc[i+1] = '-1'

        while '-1' in abc:
            abc.remove('-1')
        if len(abc) < n:
            n = len(abc)
        N -= 1


    result = len(abc)


    print("#{} {}".format(tc, result))