import json


def average(scores):
    total = 0
    
    for i in scores:
        total += i
    result = total / len(scores)

    return result

    # 여기에 코드를 작성합니다.


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores_json = open('problem01_data.json')
    scores = json.load(scores_json)
    print(average(scores)) 
    # => 82.5