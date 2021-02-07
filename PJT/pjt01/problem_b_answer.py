import json
from pprint import pprint



def movie_info(movie, genres):

    result = {}
    genre_names = []

    overview = movie.get('overview')
    ID = movie.get('id')
    title = movie.get('title')
    poster_path = movie.get('poster_path')
    vote_average = movie.get('vote_average')
    genre_ids = movie.get('genre_ids')

    for genreA in genre_ids:
        for genreB in genres_list:

            # if genreA == genreB: 
            #    genre_names.append(genres_list['name']) -> 이렇게 하니 genre_names에 아무것도 추가가 되지 않는다.
            if genreA == genreB['id']:  #-> why id? genre_list 에 숫자를 부르는 key 값
                genre_names.append(genreB['name'])
           # genre_names = genres_list.get('name') -> genres_list가 list라서 안되네 그러면 genre_names도 list로 바꾸고
           # list 추가를 해야겠다.

    

    

    


    result['overview'] = overview
    result['ID'] = ID
    result['title'] = title
    result['poster_path'] = poster_path
    result['vote_average'] = vote_average
    result['genre_names'] = genre_names


    return result


# 우선 받은 데이터를 프린트해보자
 # print(movie, type(movie)  -> dict
 # print(genres, type(genres_list))  -> list
 # 제공된 데이터에서 id, title, poster_path, vote_average, overview, genre_ids
 # 키에 해당하는 정보만 가져옵니다.  <-- 요거는 A문제에서 movie_dict -> movie 로만 바꾸면 가능함
 # genre_ids를 genre_names로 변환하여 dictionary에 추가합니다.
 # 우선 genre_ids를 딕셔너리로 바꿔서 
 # 번호에 맞게 
 # 'genre_ids': [80, 18]   ->  'genre_names :  ['Crime', 'Drama'] 이렇게 해야함
 # 'genre_ids' 는 리스트다. genres_list 도 리스트다.
 # 'genre_ids 의 숫자와 genres_list의 숫자가 같으면 key 값인 'name'을 이용해서 value값을 꺼내고
 #  그 값을 새로운 dict genre_names에 저장한다. 





        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))