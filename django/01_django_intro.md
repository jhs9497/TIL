# Django Intro

> 5기 광주 1반만을 위한 요약 자료입니다.
>
> 여러분만 보세요 :)

[toc]

## 설치하기

> 설치 후 확인은 pip list 명령어를 통해 확인 가능합니다ㅏ.

```bash
$ pip install django
```



## 프로젝트 생성하기

방법 1. 새로운 폴더를 만들고 그 안에 생성하기

```bash
$ python manage.py startproject first_project
```



방법 2. 현재 위치에 생성하기

> 명령어 맨 뒤에 점을 찍으면 현재 위치에 모든 Django 파일이 생성됩니다..

```bash
$ python manage.py startproject 프로젝트명 .

ex)
$ python manage.py startproject config .
```



## 서버 실행하기

> 항상 현재 위치에 `manage.py` 파일이 있는지 확인하세요!

```bash
$ python manage.py runserver
```



## 요청-응답 연습

- 간단한 메세지 응답하기
  1. url 정의
  2. view 함수 정의
  3. 메세지 응답

- **HTML 파일 응답하기**
  1. url 정의
  2. view 함수 정의
  3. templates 폴더 및 HTML 파일 작성



## 코드 작성 순서

> 코드 작성 순서는 UVT, UVT, UVT...!
>
> **URL을 통해 요청을 받아서,** 
> **HTML 파일을 응답으로 보내줘야함을 항상 기억해주세요.**

1. urls.py (U)

   - 사용자가 우리 서버로 요청할 수 있는 URL을 정의하는 파일
2. views.py (V)
   - 사용자의 요청을 처리하는 함수가 작성되는 파일
- **모든 view 함수의 첫번째 인자에는 반드시 request 인자가 들어옵니다.**
3. templates (T)

   - 응답으로 보내줄 HTML 파일이 담기는 폴더

   - 폴더명은 **반드시 templates**로 작성해야 Django가 찾을 수 있습니다.



## 앱 생성

Django에서 App이란?

- 하나의 장고 프로젝트는 **여러 개의 앱**을 가질 수 있습니다.

- **기능별로 분리**해서 코드를 작성하면 프로젝트를 관리하기 쉽다는 장점이 있습니다.
- **각 앱은 자신만의 UVT를 가집니다**. 즉, 자신만의 urls.py, views.py, 그리고 templates 폴더를 관리합니다.



앱 생성하기

```bash
$ python manage.py startapp articles
```



앱 등록하기 (중요)

> Tip. 항상 리스트의 마지막 요소 뒤에 trailing comma를 찍어주세요.

```python
# settings.py

installed_apps = [
  'articles',
]
```



urls.py 수정하기

> 프로젝트 폴더란?
>
> settings.py 파일이 있는 폴더를 뜻합니다.



> 중요 Tip.
>
> urls.py는 프로젝트 폴더와 각 앱 내부 모두에 존재할 수 있습니다.
>
> 처음에는 많이 헷갈릴 수 있지만, **모든 사용자의 요청은 프로젝트 폴더 안에 있는 urls.py로 들어오게 됩니다.** 
>
> 그리고 **이 urls.py가 각 앱에 있는 urls.py로 분배**해주는 역할을 담당하게 됩니다.

```python
# 프로젝트폴더/urls.py
from 프로젝트폴더명.articles import views

urlpatterns = [
  # 실제 요청이 들어오는 경로
  # http://localhost:8000/articles/ 
  
  # articles/라는 경로로 요청이 들어왔을 때
  # articles 앱의 views.py에 작성된 index 함수에서 처리하겠다는 뜻입니다.
  path('articles/', views.index),
]
```

- 절대 경로? 상대 경로?

  - 현재 URL에서의 루트 경로는 다음과 같습니다.

    ```
    http://localhost:8000/
     
    # ex. 네이버의 루트 경로
    https://naver.com/
    
    # ex. 구글의 루트 경로
    https://google.com
    ```

  - **절대 경로**는 **루트 경로부터 이어지는 경로**를 모두 다 적는 것을 말합니다.

  - **상대 경로**는 **루트 경로는 생략**하고, 현재 경로에서부터 작성하는 것을 말합니다. Django에서는 상대 경로를 주로 사용할 예정입니다.



## Variable Routing

> 요청 URL의 일부분을 변수화하여 사용하는 것을 말합니다.
>
> 하나의 URL로 다양한 작업을 할 수 있다는 장점이 있습니다.

코드 작성 순서 및 주의사항

1. urls.py 작성

   - URL의 일부분을 문자 또는 숫자 타입의 변수로 지정합니다.

     ```python
     # 문자 타입으로 변수화
     articles/<str:name>/
       
     # 숫자 타입으로 변수화
     articles/<int:number>/
     ```

2. views.py 수정

   - 반드시 함수의 매개변수로 urls.py에 작성한 이름의 변수명을 적습니다.
   
     ```python
     # views.py
     
     def index(request, number):
       	pass
     ```
   
     

## URL 분리

> 프로젝트 폴더의 urls.py에서 각 앱의 urls.py로 요청 전달하기



Django에서의 요청 전달 흐름

1. **모든 요청은 최초에 프로젝트 폴더의 urls.py로 전달**됩니다.
2. **프로젝트폴더/urls.py**에서 **각 앱의 urls.py로 분배**합니다.
3. **각 앱의 urls.py**에서 URL에 연결된 **뷰 함수를 실행**시킵니다.



include 함수 사용

- 게시글 관련된 모든 요청을 articles 앱으로 **전달**하는 경우

```python
# 프로젝트폴더/urls.py
from django.urls import path, include

urlspatterns = [
  path('articles/', include('articles.urls')),
]
```



articles 앱의 urls.py 작성

```python
# articles/urls.py

from django.urls import path
from . import views

urlspatterns = [
  path('articles/', views.index),
]
```



## Form - 웹 애플리케이션에서 Form 태그가 가지는 의미

- 웹 애플리케이션에서 Form이 유독 큰 의미를 가지는 건, **사용자에게 어떤 정보를 입력받는 유일한 매개체이기 때문입니다.**
- Form 태그는 사용자가 입력한 어떤 값을 담아서 Django 서버로 전달해주는 역할을 합니다. 
- 예를 들어, 블로그에서 글을 작성할 때 사용자에게 보여주는 화면에는 반드시 form이 필요합니다.



## Form의 구조

- `action`: 폼에 담긴 정보를 보낼 주소.
- `methods`: 요청의 종류 (단, Form 태그는 4가지 요청 중 GET, POST만 가능하다.)
  - [TMI] 개발자들은 사용자 요청의 종류를 HTTP methods라는 이름으로 분류해놓았습니다.
    1. 어떤 정보를 보고 싶을 때 (GET)
       - ex) 네이버 메인으로 접속하는 경우
       - ex) 네이버에서 검색하는 경우
    2. 어떤 정보를 추가하고 싶을 때 (POST)
       - ex) 블로그에 글을 쓰는 경우
    3. 어떤 정보를 삭제하고 싶을 때 (DELETE)
       - ex) 블로그 글을 삭제하는 경우
    4. 어떤 정보를 수정하고 싶을 때 (PUT/PATCH)
       - ex) 블로그 글을 수정하는 경우
- `input`: 실제 사용자의 입력값이 담기는 부분
  - **input[name]:** 서버에서 input 태그에 접근할 때 사용할 이름. 어떤 양식에서 칸의 이름에 해당한다고 보면됨.
  - **input[value]**: input 태그에 실제로 담기는 값. 어떤 양식의 칸에 실제로 적힌 내용.
- `label`: name과 비슷하나, name 속성은 서버(개발자)를 위한 것이고, label은 해당 칸의 이름을 사용자에게 보여주기 위한 용도.
- `submit`: 제출 버튼으로써, 제출 버튼을 눌러야지만 폼이 전송.



## Template Namespace

- Django는 템플릿(HTML 파일)을 찾을 때 각 앱의 templates 폴더를 들여봅니다.
- 이 때, 찾는 순서는 `**installed_apps`에 등록된 이름 순서대로** 찾게 되며 가장 먼저 찾게되는 템플릿을 사용합니다.
- 만약 **여러 앱에서 동일한 이름의 템플릿 파일이 존재할 경우**(ex. index.html), 가장 먼저 등록된 앱의 템플릿을 사용합니다.
- **따라서 이를 해결하기 위해 의도적으로 상위 폴더를 하나 둠으로써, 각 앱 별로 templates 폴더를 구분해줍니다.**





