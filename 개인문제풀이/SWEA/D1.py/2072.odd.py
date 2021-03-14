test_case = int(input())

for i in range(1, test_case+1):

    numbers = list(map(int, input().split()))


    total = 0
    for j in numbers:
        
        if j % 2 == 1:
            total += j
      

    print(f'#{i} {total}')










