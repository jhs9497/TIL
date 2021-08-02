def hanoi (n,start,assist,end):
    if n == 1:
        print(f'{n} : {start} -> {end}')
        return
    else:
        hanoi(n-1, start, end, assist)
        print(f'{n} : {start} -> {end}')
        hanoi(n-1, assist, start, end)

hanoi(int(input()),1,2,3)