import json
from pprint import pprint


def movie_info(movies, genres):

    # movies 와 genres를 프린트해본다
    # print(movies, type(movies))   -> list
    # print(genres, type(genres))   -> list
    # 만들어야 할 함수 : movies에 들어있는 20개의 영화를 
    # 'genre_names' , 'id' , 'overview' , 'poster_path' , 'title' , 'vote_average'
    # 의 정보만 추출되도록 만든다.
    # 1. genre_names는 차치하고 5개 먼저 추출할 수 있도록 해보자
    # 2. 빈 리스트를 만들고 A 풀듯이 한다.
    
    # print(movies[2], type(movies[2])) -> 이렇게 하니깐 3번째 영화가 출력된다. 그리고 dict...!

    # 3번째 영화의 overview 를 출력하려면 ?

    #result = {}

    #overview = movies[2].get('overview')

    #result['overview'] = overview

    #print(result)   ---> 된다!!

    # 그럼 3번째 영화의 genre_names를 출력하려면 ?

    #genre_names = []

    #genre_ids = movies[2].get('genre_ids')

    #for genreA in genre_ids:
        #for genreB in genres_list:
            #if genreA == genreB['id']:
                #genre_names.append(genreB['name'])

    #print(genre_names)  <--- 된다!!!

    # 인덱싱으로 해보자
    # print(movies[:], type(movies[:])) <---- GREAT!

    # 'genre_names' , 'id' , 'overview' , 'poster_path' , 'title' , 'vote_average'

    result = {}
    genre_names = []

    overview = movies[:].get('overview')
    ID = movies[:].get('id')
    title = movies[:].get('title')
    poster_path = movies[:].get('poster_path')
    vote_average = movies[:].get('vote_average')
    genre_ids = movies[:].get('genre_ids')          

    for genreA in genre_ids:
        for genreB in genres_list:

           
            if genreA == genreB['id']:  
                genre_names.append(genreB['name'])
           


    result['overview'] = overview
    result['ID'] = ID
    result['title'] = title
    result['poster_path'] = poster_path
    result['vote_average'] = vote_average
    result['genre_names'] = genre_names


    return result
















# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))