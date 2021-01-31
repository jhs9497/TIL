import requests
from tmdb import URLMaker
from pprint import pprint


def recommendation(title):
    TMDB_id = URLMaker('fb9a96092cd1259e59917287f35839c8').movie_id(title)
    # title을 받아 해당 movie의 id값을 구합니다.
    
    url = URLMaker('fb9a96092cd1259e59917287f35839c8').get_url('movie/{movie_id}', 'recommendations', reigon = 'KR', language = 'ko')

    response = requests.get(url)

    
    return result_list

    


    
if __name__ == '__main__':
    # 제목 기반 영화 추천
    pprint(recommendation('기생충'))
    # =>   
    # ['원스 어폰 어 타임 인… 할리우드', '조조 래빗', '결혼 이야기', '나이브스 아웃', '1917', 
    # '조커', '아이리시맨', '미드소마', '라이트하우스', '그린 북', 
    # '언컷 젬스', '어스', '더 플랫폼', '블랙클랜스맨', '포드 V 페라리', 
    # '더 페이버릿: 여왕의 여자', '두 교황', '작은 아씨들', '테넷', '브레이킹 배드 무비: 엘 카미노']
    pprint(recommendation('그래비티'))    
    # => []
    pprint(recommendation('id없는 영화'))
    # => None
