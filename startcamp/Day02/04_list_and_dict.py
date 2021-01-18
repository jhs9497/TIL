movie = {
    'movieInfo': {
        'movieNm': '광해, 왕이 된 남자',
        'movieNmEn': 'Masquerade',
        'showTm': '131',
        'prdtYear': '2012',
        'openDt': '20120913',
        'typeNm': '장편',
        'nations': [
            {
            'nationNm': '한국'
            }
        ],
        'genres': [
            {
            'genreNm': '사극'
            },
            {
            'genreNm': '드라마'
            }
        ],
        'directors': [
            {
            'peopleNm': '추창민',
            'peopleNmEn': 'CHOO Chang-min'
            }
        ],
        'actors': [
            {
            'peopleNm': '이병헌',
            'peopleNmEn': 'LEE Byung-hun',
            'cast': '광해/하선'
            },
            {
            'peopleNm': '류승룡',
            'peopleNmEn': 'RYU Seung-ryong',
            'cast': '허균'
            },
            {
            'peopleNm': '한효주',
            'peopleNmEn': 'HAN Hyo-joo',
            'cast': '중전'
            }
        ]
    }
}

## 내가 숙제로 한 코드##

print(movie['movieInfo']['nations'][0]['nationNm'])

# 1. 영화의 제목을 출력하시오.
print(movie['movieInfo']['movieNm'])

# 2. 다음 movie의 감독의 영어 이름을 출력하시오.

# 왜 movie 에서 에러가 뜨지 ?
PeopleNmEn = movie['movieInfo']['directors']['PeopleNmEn']
print(movie['movieInfo']['directors'])

# 3. 다음 movie의 배우의 인원을 출력하시오.
actors = movie['movieInfo']['actors']
print(len(actors))

## 정답 풀이 ##

movie_title = movie['movieInfo']['movieNm']
print(movie_title)

director_name = movie['movieInfo']['directors'][0]['peopleNmEn']  #-< 0을 붙히는 이유는 {} 딕셔너리를 벗기기 위해서

print(director_name)

actor_list = movie['movieInfo']['actors']
num_of_actors = len(actor_list)
print(actor_list)
print(num_of_actors)