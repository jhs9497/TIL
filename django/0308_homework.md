### 1. settings

```django
TIME_ZONE = 'Asia/Seoul'

USE_TZ
```



### 2. urls

```django
'write/', views.write
```



### 3-1

>menus 리스트를 반복문으로 출력하시오.

```django
{% for menu in menus %}
    <li>{{ menu }}</li>
{% endfor %}
```



### 3-2

> posts 리스트를 반목문을 활용하여 0번 글부터 출력하시오.

```django
{% for post in posts %}
  <p>{{ forloop.revcounter0 }}번 글 : {{ post }}</p>
{% endfor %}
```



### 3-3

> users 리스트가 비어있다면 현재 가입한 유저가 없습니다. 텍스트를 출력하시오.

```django
{% for user in users %}
    <p>{{ user }}</p>
{% empty %}
    <p>현재 가입한 유저가 없습니다.</p>
{% endfor %}
```



### 3-4

> 첫 번째 반복문일 때와 아닐 때를 조건문으로 분기처리 하시오.

```django
{% if forloop.first %}
    <p>첫 번째 반복문 입니다.</p>
{% else %}
    <p>첫 번째 반복문이 아닙니다.</p>
{% endif %}
```



### 3-5

> 출력된 결과가 주석과 같아지도록 하시오

```django
<!--5-->
<p>{{ 'hello'|length}}</p>
<!--My Name Is Tom-->
<p>{{ 'my name is tom'|capfirst}}</p>
```



### 3-6

> 변수 today에 datetime 객체가 들어있을 때 출력된 결과가 주석과 같아지도록 하시오

```django
<!-- 2020년 02월 02일 (Sun) PM 02:02-->
{{ today|date:"Y년 m월 d일 (D) A h:f"}}
```



### 4-1

1. 지문의 코드 중 form 태그의 속성인 action의 역할에 대해 설명하시오.
   - 기본 url + /create/에 input받은 값들을 전달한다
2.  지문의 코드 중 method가 가질 수 있는 속성 값을 작성하시오.
   - GET

3. input 태그에 각각 `안녕하세요`, `반갑습니다`, `파이팅` 문자열을 넣고 submit  버튼을 눌렀을 때 이동하는 url 경로를 작성하시오.
   - http://127.0.0.1:8000/create/?title=안녕하세요&content=반갑습니다&my-site=파이팅



### 5 로또 무작위 추첨 페이지

