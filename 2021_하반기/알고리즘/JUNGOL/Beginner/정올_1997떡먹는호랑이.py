D, K = map(int, input().split())

def tiger(n):
    if n == D:
        return K

    return tiger(n) + tiger(n+1)


print(tiger(6))