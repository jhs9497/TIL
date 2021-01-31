import requests
from tmdb import URLMaker
from pprint import pprint
# 가져온 자료를 좀 더 이쁘게 보고 싶응니 pprint를 import하자


def popular_count():
    url =URLMaker('fb9a96092cd1259e59917287f35839c8').get_url('movie', 'popular', reigon = 'KR', language = 'ko')
    # tmdb.py의 클래스 함수를 이용하여 발급받은 내 키를 넣은 url주소를 만든다.
    response =requests.get(url) # response변수를 만든 후 requests모듈을 이용하여 url을 vscode로 가져온다

    # pprint(result)
    # response를 pprint하면 응답값이 200이 나온다.

    # movie_dict = result.text
    # movie_dict라는 새로운 변수에 response를 넣는다
    # text로 뽑아도 볼 순 있지만 좀 더 다루기 쉽게 (dict형으로) json 형식으로 뽑는다
    movie_dict = response.json()

    # for movie in movie_dict:
        # print(movie)
    # -> 이렇게 for문을 돌려보면 page / results  total_pages / total_results 가 나온다.
    # 우리가 필요한 정보는 results이므로
    movie_list = movie_dict.get('results')
    # 이렇게 새로운 movie_list를 만든다.
    # 그리고 for문을 돌려보면 영화 정보들이 잘 나온다는 것을 알 수 있다.

    # 영화의 총 개수는 movie_list의 len값과 같으므로

    return len(movie_list)



if __name__ == '__main__':
    print(popular_count())