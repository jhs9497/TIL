import requests
from tmdb import URLMaker
from pprint import pprint


def vote_average_movies():
    url =URLMaker('fb9a96092cd1259e59917287f35839c8').get_url('movie', 'popular', reigon = 'KR', language = 'ko')
    response =requests.get(url)
    movie_dict = response.json()
    movie_list = movie_dict.get('results')

    # 앞에 부분은 A와 같다.

    # movie_list에서 평점에 접근하려면 ??
    # movie_list는 큰 리스트 안에 20개의 영화정보가 들어있고 각각의 영화정보는 
    # 딕셔너리로 구성되어 있다. 우선 0번째 영화정보의 평점을 뽑아보자


    # print(movie_list[0]['vote_average'])
    # 오케이 잘 뽑힌다. 그러면 [0]을 for문의 i로 인덱싱하여 각 영화들의 평점을 뽑을 수 있고
    # 그것을 기준으로 영화의 정보도 뽑을 수 있다. 
    # how? 뒤에 'vote_average만 빼면 각 영화의 전체 정보이다
    result_list = []
    # 정답을 담을 빈 리스트를 만든다.
    for i in range(len(movie_list)):
        # 영화의 전체 길이를 기준으로 for 문을 돌리면 i는 0~19까지의 숫자로 돌아가고
        if movie_list[i]['vote_average'] >= 8:
            # 명세에 나온대로 i번째 영화의 평점이 8이상이면
            result_list.append(movie_list[i])
            # result_list에 append함수를 이용하여 i번째 영화의 정보를 넣는다
    return result_list





if __name__ == '__main__':
    pprint(vote_average_movies())




#정답

# movie_list = movie_dict.get('results')
#     top2 =  [] 
#     for z in range(len(movie_list)):
#         a = movie_list[z]['vote_average']
#         if a >= 8.0:
#             top2.append(movie_list[z])
#     return top2
