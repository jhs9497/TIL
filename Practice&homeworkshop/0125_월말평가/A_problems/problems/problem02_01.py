import json


def over(movie):
    rate = movie['user_rating']
    if rate >= 8:
        return True
    return False
    # 여기에 코드를 작성합니다.


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('problem02_data.json', encoding='UTF8')
    movie = json.load(movie_json)
    print(over(movie)) 
    # => True