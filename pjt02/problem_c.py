import requests
from tmdb import URLMaker
from pprint import pprint


def ranking():
    url =URLMaker('fb9a96092cd1259e59917287f35839c8').get_url('movie', 'popular', reigon = 'KR', language = 'ko')
    response =requests.get(url)
    movie_dict = response.json()
    movie_list = movie_dict.get('results')

    # 앞에 부분은 A,B 와 같다.

    # 영화의 평점을 출력하는 방법은 B와 같다.

    # 금요일날 TOP 5를 출력하는 방법은 알아냈지만 높은 평점 순으로 TOP5를 끊어서
    # 출력하는 법은 해내지 못하였다. 어떻게 하면 가능할까

    # 각 영화의 인덱싱은 유지하면서 높은 평점부터 차례로 새로운 list에 집어넣어야 한다?
    # 우선 쓸만한 list 함수는 .sort()와 .reverse()

    # 1) 각 영화의 평점만 뽑아 새로운 top5_list를 만든다.
    # 2) top5_list를 sort와 reverse를 통해 높은 평점 순으로 정렬시킨다.
    # 3) 정렬된 top5_list를 for문으로 돌리고 movie_list[i]['vote_average']도 이중 for문으로 돌린다
    # 4) top5_list의 평점이 높은 순대로 movie_list[i]['vote_average']을 돌면서 평점이 같은지 확인한다.
    # 5) Answer_list를 새로 만든 후 평점이 같은 경우 각 영화의 전체 정보를 새로운 Answer_list에 추가한 후 답을 도출한다.
    # 6) 이런 경우 점수가 같을 경우 중복된 영화가 추출될 수 있으므로 .pop()을 통해 없애버린다

    average_list = []
    for i in range(len(movie_list)):
        average_list.append(movie_list[i]['vote_average'])
    # 각 영화의 평점만을 뽑은 average_list를 만들었다.

    average_list.sort()
    # 리스트를 정렬한다. 낮은 점수부터 정렬되있을 것이다.
    average_list.reverse()
    # 반대로 정렬하여 높은 점수부터 나오게 만든다.
    top5_list = average_list[0:5]
    # 정렬된 average_list에서 5개만 뽑은 top5_list를 만든다.
    # print(top5_list)
    # 확인


    Answer_list = []
    # 최종 답을 담을 Answer_list를 만든다.
    for score in top5_list:
        # top5_list에서 for문 하나 돌리고
        for i in range(0, 20):
            # 0~19까지 for문 이중으로 돌리면서
            if score == movie_list[i]['vote_average']:
                # 만약 top5_list의 score가 movie_list의 i번째 평점과 같으면
                Answer_list.append(movie_list[i])
                # Answer_list에 그 i번째 movie_list정보를 추가하면서
                # movie_list.pop(i)  --> pop을 했더니 기존 movie_list가 훼손 되어서 IndexError: list index out of range 에러가 난다.
                # movie_list에서 i번째 정보는 pop한다. why? 평점이 같을 경우 앞에 있는 한 영화만 나올테니깐
    return Answer_list

    

    # 최종으로 정답 도출 8.5 8.4 8.3 7.7 7.4 영화의 정보가 차례로 나와야한다.
    # 우선은 잘 나왔다 성공!



    










if __name__ == '__main__':
    # popular 영화 평점순 5개 출력
    pprint(ranking())



