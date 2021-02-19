for tc in range(1, int(input())+1):
    A, B = input().split()  #6  #4

    if len(B) == 1:  # B의 길이가 1이면 바로 A의 길이만큼 프린트
        print('#{} {}'.format(tc, len(A)))
        break
    else:
        count = 0 # A랑 B가 같으면 +1 씩
        idx = 0 # A의 탐색 시작 인덱스 (계속 움직여야)
        a = len(A) # A의 길이이자 남은 A열의 길이로 사용하자
        b = len(B)
        while a >= b: # A의 길이가 B보다 커져버리면 의미가 없으므로
            A_ = '' # A 패턴 후보군
            for i in range(idx, idx+b): # idx값이 변화하면서 A의 인덱싱을 조절함
                A_ += A[i]
            B_ = '' # 고정된 B 패턴
            for j in range(b): # B는 항상 고정
                B_ += B[j]

            if A_ == B_: # 만약 A랑 B의 패턴이 같다면
                count += 1 # count +1 해주고
                idx += b # 시작 인덱스를 b만큼 뛰어넘어줘야함 why? 만약 A = AOAOAOAOAOAOA B = AOA이면 뛰어넘지 않을시 중첩
                a -= b # 뛰어 넘은만큼 남은 A의 길이도 b로 빼준다
            else: # 값이 다르다면
                idx += 1  # 다음 칸을 탐색한다
                a -= 1

    answer = len(A)- count*len(B) + count

    print('#{} {}'.format(tc, answer))