def solution(s):
    # 우선 입력받은 s문자열이 홀수면 무조건 실패하므로 return 0
    if len(s) % 2 != 0:
        return 0

    # stack을 이용해서 풀어보자
    stack = []
    # s문자열을 돌면서
    for i in s:
        # 만약 stack이 비어있으면
        if not stack:
            # 무조건 stack에 i 값 추가
            stack.append(i)
        else:
            # 만약 i값이랑 stack 맨 위에 값이 같으면 서로 짝지어서 없앨 수 있으므로
            if i == stack[-1]:
                # stack 맨 위 친구 pop으로 없애기
                stack.pop()
            else:
                # 같지 않으면 stack에 i값 추가
                stack.append(i)

    # for문 다 돌고 나서 만약 stack에 뭐라도 존재하면 실패이므로
    if stack:
        # 0 출력
        return 0
    # 아무것도 없다면 성공이므로 1출력
    return 1