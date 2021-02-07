## PJT01



#### 문제 1️⃣

>제공된 데이터에서 id, title, poster_path, vote_average, overview, genre_ids
>키에 해당하는 정보만 가져옵니다



#### 완성 코드

```python
def movie_info(movie):

        # 과감하게 낮에 했던거 다 지웠음
        # 처음부터 다시
        # movie_dict에 뭐가 들어있는지 출력부터 해보자
        # print(movie_dict) -> dic 안에 다양한 key : value가 들어있다.
        # 내가 원하는건 이 중에 id, title, poster_path, vote_average, overview, genre_ids의 key & value
        # 우선 overview만 뽑아낸다고 생각해보고 id의 value 값을 뽑아보자
        # print(movie_dict['overview']) 오케이 잘나옴
        # overview의 values값과 대응하는 key값을 새로 만들어서 새로운 dict에 담아보자
        
        result = {}

        overview = movie_dict.get('overview')

        result['overview'] = overview

        print(result)

        # 오케이 성공 나머지도 똑같이 만들고 print말고 return으로 반환하자

        ID = movie_dict.get('id')
        title = movie_dict.get('title')
        poster_path = movie_dict.get('poster_path')
        vote_average = movie_dict.get('vote_average')
        genre_ids = movie_dict.get('genre_ids')

        result['ID'] = ID
        result['title'] = title
        result['poster_path'] = poster_path
        result['vote_average'] = vote_average
        result['genre_ids'] = genre_ids


        return result


       # 성공
```



#### 느낀점 😅

> 우선 처음에 잘 이해되지 않았던 것 같다. 항상 리스트나 딕셔너리가 눈에 보이는 상태에서 풀다가 갑자기 없는 상태에서 풀고자 하니 벙쪘다었다. 데이터 받은 부분을 프린트로 확인하고 나니 조금은 눈에 보였다.
>
> 
>
> 낮에 할 때는 라이브강의 때 풀었던 문제랑 유사해서 꽤나 빠르게 풀 수 있었다. 사실 필기한 내용을 바탕으로 하다보니 이해하면서 풀었다기 보다고 볼 수 없을 것 같기도 하다. 저녁에 다시 해보자란 생각으로 일부러 다 지우고 다시 풀어봤다. 생각보다 잘 안되어서 딕셔너리 파트 라이브방송을 한 번 더 시청하고 풀어보았다. 조금은 길이 보이는 듯한 기분이 들었다. 결국 오래걸리긴 했지만 스스로의 힘으로 문제를 풀어내서 기쁘긴하다.. 다만 지금 시간이 예상보다 너무 많이 소요되서 걱정이다 하하



#### 문제 2️⃣

> genres.json파일을 이용하여 genre_ids를 genre_names로 변환하여
> dictionary에 추가합니다.



#### 완성코드

```python
mport json
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
```



#### 느낀점 🤐

> A번의 경험을 살려서 비교적 접근을 가까이 가긴 했지만..... genre_names도 dic이라는 생각에 사로잡혀있다가 시간을 너무 많이 날렸다. 
>
> **\# if genreA == genreB: **
>
> **\#  genre_names.append(genres_list['name']) -> 이렇게 하니 genre_names에 아무것도 추가가 되지 않는다.**
>
> **if genreA == genreB['id']: #-> why id? genre_list 에 숫자를 부르는 key 값**
>
> **genre_names.append(genreB['name'])**  
>
> 이 부분에서 너무 막혀서 답답하여 결국 교수님께서 라이브강의 때 짜준 코드를 훔쳐봤..



#### 문제 3️⃣

> 영화 전체 정보를 수정하여 반환하는 함수 movie_info를 완성합니다.



#### (미)완성코드

```python
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

    overview = movies[0].get('overview')
    ID = movies[0].get('id')
    title = movies[0].get('title')
    poster_path = movies[0].get('poster_path')
    vote_average = movies[0].get('vote_average')
    genre_ids = movies[0].get('genre_ids')          

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
```



#### 느낀점 😡

> 다 됐다 ! 풀었다 ! 라고 생각하고 했는데 안되니 화가 매우났다 ㅋㅋㅋ 
>
> overview = movies[0].get('overview') 이 부분에서 인덱싱 [0] 을 지정하니 그에 해당하는 첫 번 째 영화
>
> 는 잘 나와서 '이제 됐다!  [:] 슬라이싱으로 전체 영화를 뽑으면 되겠군!' 했는데 에러가 떴다....
>
> 출력예시를 보니 결국 리스트로 전체가 출력되는걸로 보아 접근이 잘못 된 것 같다..
>
> 하지만 12시가 제출마감시간이라는 핑계를 대며 내일로 미뤄본다..

