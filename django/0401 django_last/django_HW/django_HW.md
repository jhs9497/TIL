# 14 homework



## 1.

1. T

2. T

3. F 역참조충돌이 우려될 시 related_name작성한다

   

## 2.

a) request.user

b) article.like_users.all



## 3.

a) user_pk

b) following

c) filter

d) remove

e) add



## 4.

class를 정의할 때 Meta class 안에 커스텀하여 사용하는 User를 model로 정의해줬어야 했는데

그 과정이 생략되어 있어서 계속 커스텀한 User모델이 아닌 이전의 User모델을 찾다보니 에러가 생긴 것 이다.



## 5.

 1:N관계에서 class끼리 역참조를 하는 경우 필드네임_set.all()과 같은 방식으로 하게 되는데 방식은 related_name을 설정안한 경우 2개 이상의 역참조끼리 다르게 행동하지않고 충돌이 발생하기 때문이다



## 6.

a) person.followings.all

b) person.followers.all

c) request.user

d) person.username

e) person.pk





# 15 homework



## 1.

1. M : model의 약자로 자료의 형태를 정의한다.
2. T : template의 약자로 웹 페이지에서 출력할 모습을 정의한다.
3. V : view의 약자로 어떤 페이지를 어떠한 동작으로 보여줄지 정의한다.



## 2.

a) articles.views

b) views

c) views.index



## 3.

a) setting.py

b) DIRS

c) STATIC_URL



## 4.

1. python manage.py makemigrations
2. python manage.py showmigrations
3. python manage.py sqlmigrate articles 0001
4. python manage.py migrate



## 5.

1. F
2. T
3. T
4. F



## 6.

MEDIA_ROOT = BASE_DIR / 'crud' / 'uploaded_files'

MEDIA_URL = '/crud/uploaded_files'



## 7. 

1. T

2. F

3. T  SQL은 세미콜론(;)을 만나기 전까지 절대 실행되지 않습니다.

4. T  `.`으로 시작하는 모든 명령어는 sqlite3 프로그램의 기능을 실행하는 명령어이며, SQL 문법에 속하지 않습니다.

5. T



## 8.

PROTECT



## 9.

a) ManyToManyField

b) related_name 

역참조 혼선 방지



## 10.

accounts_user_followings

from_user_id

to_user_id

