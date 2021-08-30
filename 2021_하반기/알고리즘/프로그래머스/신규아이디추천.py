str_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '_', '.']

def solution(new_id):
    # 1단계 소문자 치환
    new_id = new_id.lower()

    # 리스트가 수정하기 편하므로 리스트로 변환
    new_id = list(new_id)

    # 2단계 알파벳, 숫자, '-', '_', '.' 제외한 문자 제거
    delete_list = []
    for i in range(len(new_id)):
        if new_id[i] in str_list:
            pass
        else:
            delete_list.append(i)

    delete_list.reverse()
    for idx in delete_list:
        new_id.pop(idx)

    # 3단계 연속된 마침표 제거
    delete_dot = []
    for i in range(len(new_id) - 1):
        if new_id[i] == '.' and new_id[i + 1] == '.':
            delete_dot.append(i)

    delete_dot.reverse()
    for idx in delete_dot:
        new_id.pop(idx)

    # 4단계 마침표가 처음에 위치하면 제거
    if new_id and new_id[0] == '.':
        new_id.pop(0)

    # 5단계 빈 문자열이면 'a'대입
    if len(new_id) == 0:
        new_id.append('a')

    # 6단계 길이가 16이상이면 길이조절 + 끝문자가 '.'이면 제거
    if len(new_id) >= 16:
        new_id = new_id[0:15]

    if new_id[-1] == '.':
        new_id.pop(-1)

    # 7단계 2자 이하라면 마지막문자를 길이가 3될때까지 추가
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id.append(new_id[-1])

    # 문자화
    answer = "".join(new_id)

    return answer


