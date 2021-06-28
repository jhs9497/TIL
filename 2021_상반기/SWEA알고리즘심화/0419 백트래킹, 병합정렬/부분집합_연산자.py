김밥 = ['단무지', '돈까스', '참치', '새우']

N = len(김밥)

for i in range(1<<N):
    for j in range(N):
        if i & (1<<j):
            print(김밥[j], end=" ")
    print()