# 피인용수가 논문수와 같아지거나 피인용수가 논문수보다 작아지기 시작하는 숫자가 바로 나의 h-index
# 우선 오름차순 정렬 + 0 제외

def solution(citations):
    citations.sort()
    C = len(citations)
    door = 'close'   # 리스트가 다 0으로 이루어진 경우 문제가 생김

    for i in range(C):
        if citations[i] != 0:
            door = 'open'

    if door == 'close':
        return 0

    for i in range(C, 0, -1):  # 갯수니깐 C부터 해야하네
        count = 0
        for j in range(C):
            if i <= citations[j]:
                count += 1
        if i <= count:
            return i

citations = [31,66]  # 각각의 논문에 대한 피인용수
print(solution(citations))
