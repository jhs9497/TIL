import json
from pprint import pprint



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





 
 

        

    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))