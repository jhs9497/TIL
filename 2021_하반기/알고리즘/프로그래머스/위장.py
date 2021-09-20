from collections import defaultdict

def solution(clothes):
    count_type = defaultdict(int)
    for cloth, cloth_type in clothes:
        count_type[cloth_type] += 1
    
    answer = 1
    for value in count_type.values():
        answer = answer * (value+1)
    answer -= 1
    return answer