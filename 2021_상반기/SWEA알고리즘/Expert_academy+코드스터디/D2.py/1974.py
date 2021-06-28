test_case = int(input())

for tc in range(1, test_case+1):
    puzzle = [list(map(int, input().split())) for _ in range(3)]

    for i in range(len(puzzle)):
        for j in range(len(puzzle)):
            for z in range(len(puzzle)):
                if puzzle[i][j] == puzzle[i][z]:
                    print('0')
                break


    for i in range(len(puzzle)):
        for j in range(len(puzzle)):
            for z in range(len(puzzle)):
                if puzzle[j][i] == puzzle[j][z]:
                    print('0')
                break

    
    
    else:
        print('1')
    

        
    

    