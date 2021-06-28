for a in range(int(input())):
    tc = int(input())
    student_score = list(map(int, input().split()))
    count = 0
    number = 0
    for i in range(1, 101):
        sample_count = 0
        for j in student_score:
            if i == j:
                sample_count += 1
        if count <= sample_count:
            count = sample_count
            number = i
    print('#{} {}'.format(tc, number))

        
