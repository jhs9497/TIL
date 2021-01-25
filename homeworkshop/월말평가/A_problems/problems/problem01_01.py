import json


def total(scores):
    total = 0
    for i in scores:
        total += i
    return total
    
    # 여기에 코드를 작성합니다.


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores_json = open('problem01_data.json')
    scores = json.load(scores_json)
    print(total(scores)) 
    # => 330