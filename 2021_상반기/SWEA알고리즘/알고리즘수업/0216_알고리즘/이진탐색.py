test_case = int(input())


for tc in range(1, test_case+1):
    P, Pa, Pb = map(int, input().split())

    Pa_count = 0
    start = 1
    end = P
    key = Pa
    c = int((start+end)/2)
    while start < end:
        Pa_count += 1
        if key == c:
            break
        elif key > c:
            start = c
            c = int((start+end)/2)
        elif key < c:
            end = c
            c = int((start+end)/2)


    Pb_count = 0
    start = 1
    end = P
    key = Pb
    c = int((start+end)/2)
    while start < end:
        Pb_count += 1
        if key == c:
            break
        elif key > c:
            start = c
            c = int((start+end)/2)
        elif key < c:
            end = c
            c = int((start+end)/2)


    if Pa_count == Pb_count:
        print("#{} 0".format(tc))
    elif Pa_count < Pb_count:
        print("#{} A".format(tc))
    else:
        print("#{} B".format(tc))
