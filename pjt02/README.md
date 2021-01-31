## PJT01



#### 문제 1️⃣

>영화 개수 카운트 기능 구현 영화 개수를 출력합니다. 완성된 기능은 향후 커뮤니티 서비스에서 제공되는 기 능으로 사용됩니다.



#### 완성 코드

```python
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


       # 성공
```



#### 느낀점 😄

> 처음 url 생성 함수를 만들 때 url =URLMaker('fb9a96092cd1259e59917287f35839c8').get_url('movie', 'popular', reigon = 'KR', language = 'ko') 이 부분이 잘 이해가 안됐지만 tmdb.py 파일을 계속 보고 순차적으로 해석하려고 노력하다 보니 이해가 되었다. 
>
> 또한 movie_list = movie_dict.get('results') 여기서 results를 추가하는 과정에서도 좀 부침을 겪었다. response.json() 파일을 브라우저에서 열어서 확인하는 방법이 기억이 나지 않아 전체적인 구조를 파악하는데 힘이 들었다. 그러던 중 movie_dict를 for문을 돌려봤을 때 나오는 값들이 page / results  total_pages / total_results 인 것을 보고 전체 구조를 이해하게 되었다. 이러한 방법이 있다는 것을 알게 되어서 기쁘다.
>
> dict구조에 대해 이젠 조금 잘 이해하고 다룰 수 있게 된 것 같아 기쁘다.



#### 문제 2️⃣

> 특정 조건에 맞는 영화 출력 popular를 기준으로 가져온 영화 목록 중 평점이 8 이상인 영화 목록을 출력하 는 기능을 완성합니다.



#### 완성코드

```python
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
```



#### 느낀점 😄

> movie_list에서 'vote_average'로 접근하는 방법이 바로 떠올라서 기뻤다. 이 부분은 저번주의 pjt01과 흡사한 것 같다. 그리고 url의 정보를 가져오다보니 금요일날 풀었을 때 return되던 영화목록과 지금 return되는 영화목록이 달라서 아 정말 실시간으로 데이터를 가져오는구나 느낄 수 있었다.
>
> 교수님께서 for문에서 range(len())을 잘 사용해야한다고 하셨는데 그 이유를 이제는 확실히 알 것 같다. 



#### 문제 3️⃣

> popular를 기준으로 가져온 영화 목록을 평점순으로 출력하는 함수를 완성합니 다. 해당 기능은 향후 커뮤니티 서비스에서 기본으로 제공되는 영화 정보로 사용 됩니다.



#### 완성코드

```python
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

```



#### 느낀점 🤔

> 처음에는 top5 영화평점 리스트를 만들고 movie_list의 영화 평점을 for문으로 돌리면서 top5 영화평점이 movie_list평점에 있느냐 있으면 결과 리스트에 더해줘라 라는 식으로 풀었었다. 하지만 그렇게 만드니 영화평점순으로 최종 결과가 출력되지 않고 초기 movie_list에 담겨있는 순서대로 top5가 나왔다.
>
> 그래서 어떻게 하면 top5평점 순서대로 영화정보를 나오게 할 수 있을까 생각하다가  이중 for문을 생각하게 되었고 정답을 도출할 수 있었다.
>
> 하지만 만약 top5평점이 8.5 8.5 7.7 7.7. 7.7 이런식으로 중복된 점수라면 평점이 8.5, 7.7인 영화중에 제일 첫번째 영화만 출력되어 사실상 2가지의 영화만 출력되는 오류가 발생한다. 그래서 pop을 이용해서 이미 출력된 영화는 본 리스트에서 없애는 시도를 하였지만  IndexError: list index out of range 에러가 났다. 아직 풀지못한 숙제이다.



#### 2주간의 파이썬 과정을 마치며

> 우선 4,5번은 풀지 못하였다. 금요일날 오전수업을 듣고 1번 문제를 잘 풀었기 때문에 4,5번도 잘 해결할 수 있을 것이라 생각했는데 역시 이틀이 지나니 하얀 백지처럼 잘 기억이 나지 않았다. 필기한 내용을 봐도 잘 이해가 되지 않아 내일 낮에 스터디원분들께 물어봐야 할 것 같다. 😂
>
> 지난 2주는 정말 빠르게 흘러갔다. 마치 당구를 처음 접했을 때 한동안 머리속에서 당구공이 굴러가는 경험을 했듯이 지난 2주동안 머리속에서 주피터화면이 계속 돌아다녔다. 거의 매일 꿈에 나왔다. 하지만 꽤나 몰입하고 열심히 공부했다고 생각했는데 생각보다 더디게 학습되는 기분이 들어서 속상하기도 했었다. SSAFY에 합격하고 제법 여유시간이 있었는데 파이썬 예습을 하고 올걸이라는 후회가 들기도 했다. 
>
> 디스코드 페어인 원종님도 나와 같이 이 쪽 분야에 백지 상태여서 디스코드에서 좀 신세한탄 ?을 하기도 했다 ㅋㅋㅋ 근데 마침 그 날 교수님께서 ''어떤 분들은 벌써 이 길이 내 길이 아닌가 ? 하는 반응도 있던데 그렇지 않아요 힘내세요' 같은 맥락의 말씀을 해주셨는데 뜨끔했다. 혹시 우리방에 왔었나 ? 내가 저런 말을 했었나 ? 하면서 말이다. 어쨌든 힘이 되는 말을 해주셔서 감사했던 기억이 난다.
>
> 막힐 때 마다 화나고 새로운 것을 이해 못할때마다 분노하지만 다행인 것은 '재밌다' 나는 학문을 위한 학문은 정말로 흥미를 못느낀다. 그렇기 때문에 대학 교육에 매우 싫증을 느꼈고 놀고 먹기만 하..였..(핑계)다. 하지만 SSAFY에서의 배움은 목적이 확실하고 내가 유용하게 쓸 수 있다는 확신이 있기 때문에 아침9시부터 6시까지 수업하고 6시30분부터 보충수업을 하고 8시~11시까지 스터디를 하여도 지루하지 않다. 시간이 재밌게 정말 빠르게 간다는 점이 신기하다. 
>
> 물론 지금 2주는 IT계에서 빙산의 빙산의 빙산의 일각에 불과하겠지만 적어도 앞으로의 배워가는 과정이 지루하고 지치진 않을 것 같다는 생각이 든다. 이러한 생각이 나의 취직관에도 영향을 주었다. 원래 취직에 대한 목표는 굉장히 두루뭉실했다.                                                                                                               1) 회사에서의 업무가 향후 시장에서 홀로서기 할 수 있는 역량을 키울 수 있는 회사 or                                                                               2)  나에게 꽤나 긴 시간동안 괜찮은 급여로 고용안정성을 줄 수 있는 회사                                                                                                                                      였는데 알아보면 알아볼수록 목표 회사가 생겼다. 
>
> 바로 카카오 or 네이버다.  목표는 높을수록 좋으니..의 마인드가 아니라 정말 저 회사를 목표 삼기로 했다.  화이팅!이다
>
> 
>
> 
>
> 새벽이라 그냥 의식흐름대로 글을 쓰게 되었는데 잘 읽히실지 모르겠습니다.. ㅎㅎ 파이썬 2주동안 정말 감사했었습니다. 인사치레로 하는 말이 아니라 라이브강의에서 이해안되던거 교수님께서 한번 더 설명해주실 때 바로 이해된 적 많습니다! 설명도 이해 잘 되게 잘해주시고 완전 초보적이고 반복적인 질문에도 언제나 친절하게 답변해주셔서 항상 감사하게 생각하고 있습니다. 교수님께서 열과 성의를 다한 보람을 느낄 수 있도록 저도 빠르게 성장하게 노력하겠습니다!^__^ 감사합니다!

