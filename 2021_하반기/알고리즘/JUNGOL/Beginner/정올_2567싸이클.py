N, P = map(int, input().split())

pattern = []
isOne = False

def function(X):
    global pattern
    global isOne
    L = len(pattern)
    if L > 1 and pattern[:L//2] == pattern[L//2:]:
        return

    elif L > 1 and pattern[-2] == pattern[-1]:
        isOne = True
        return

    else:
        X = X * N % P
        pattern.append(X)
        function(X)

function(N)

if isOne == True:
    print(1)
else:
    print(len(pattern) // 2)

