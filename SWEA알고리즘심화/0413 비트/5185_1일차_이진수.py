def check(X):
    global answer
    Nibble = ''
    for i in range(3):
         Nibble += str(X % 2)
         X = X // 2
    Nibble += str(X)
    Nibble = Nibble[::-1]
    answer += Nibble


for tc in range(1, int(input())+1):
    N, Hexa = input().split()
    answer = ''
    for i in Hexa:
        if i.isdigit():
            check(int(i))
        else:
            check(ord(i)-55)
    print('#{} {}'.format(tc, answer))
