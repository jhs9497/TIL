import json


def check(data):
    # 리스트, 리스트 안에 리스트
    New_check = []
    for check in data:
        New_check += check

    total = 0
    for i in New_check:
        if i >= 37.5:
            total += 1
        else :
            total = 0
        if total == 3:
            return True
    else:
        return False
        

        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    temperature_json = open('problem03_data.json', encoding='UTF8')
    temperature_list = json.load(temperature_json)
    print(check(temperature_list))
    # => True