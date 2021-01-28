import json


def rotate(data):
    New_dict = {}
    
    am = []
    pm = []
    for check in data:
        am.append(check[0])
        pm.append(check[1])
    New_dict['am'] = am
    New_dict['pm'] = pm
    return New_dict


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    temperature_json = open('problem03_data.json', encoding='UTF8')
    temperature_list = json.load(temperature_json)
    print(rotate(temperature_list))
    # => {
    #     'am': [36.7, 36.9, 37.8, 36.7, 36.3, 36.5, 36.8], 
    #     'pm': [36.5, 37.5, 37.8, 36.5, 36.4, 36.5, 36.6]
    # }
