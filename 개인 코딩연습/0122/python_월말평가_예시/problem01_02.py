import json


def over(scores):
    count = 0
    for i in scores:
        if i >= 60:
            count += 1
        result = count
    return result


    # 여기에 코드를 작성합니다.


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores_json = open('problem01_data.json', encoding='UTF8')
    scores = json.load(scores_json)
    print(over(scores)) 
    # => 3