for tc in range(1, int(input())+1):
    A = list(input().split())
    number = []
    for a in range(len(A)):
        if A[a] == '+' or A[a] == '-' or A[a] == '*' or A[a] == '/' or A[a] == '.':
            number.append(A[a])
        else:
            N = int(A[a])
            number.append(N)

    print(number)