# 장고 게시판 만들기

```
아 처음에 config와 같은 자리에 템플릿을 만들고 base.html 을만들고
config의 셋팅즈에 가서 , 
템플릿에 , DIRS : [] 여기에 , 
'DIRS': [BASE_DIR / 'templates'] 요런식으로 저장하고 
{% extends 'base.html' %} 각 html에 이렇게 익스텐즈를 해준다.

저 base는 말 그대로 화면의 뼈대를 만들어 주는것 
```





```
앞서 했던 것을 다 한다음에, 

내가 사용자로부터 요청받을 페이지를 만든다 html (앱에 저장된)
거기에 들어가서, 부트스트랩 등으로 내가 원하는 양식을 받아서 만든다
여기서 주의할 점은, label , id, name 은 다 title 혹은 , content로 바꿔준다.(각각 맞게)

요청받을 화면은 그냥 views에서 다른 것과 같게 함수하고 , 리턴하면 된다 .
이제 내가 요청을 받고, 보내줄 응답할 창을 만들어 줘야하는데, 
다시 새로운 html파일을 만들고

views에 title , content라는 변수에 title = request.GET.get('title') 이런식으로 
불러온다 content도 마찬가지. 

 article = Article(title=title, content=content) 
 이런식으로 내가 모델에 정의한 클래스를 호출하면서 클래스의 title에 내가만든 title을 저장
 article.sava() 저장을 해주고 
 
 context에 따로 딕셔너리 형태로 넣으면서 , return에 저장
```

```
이제 요청받은 페이지에서 입력을 받으면 내가 보여줄 화면으로 자동으로 넘겨줘야하는데

form 액션을 이용해서 <form action="{% url 'articles:write' %}" method='GET'> 
이렇게 보내주면 끝

<button  type="submit" class="btn btn-primary">Submit</button> 이게 있어야
아마 넘어가는 듯?



<h1>{{ article.title }}</h1>
<p>{{ article.content }}</p> 이렇게하면 요청받은걸 응답해서 보여줌

클래스로 넘겼(?)기 때문에 데이터베이스에도 저장이 된다.

```



```
GET 대신에 POST를 쓰려면
<form action="{% url 'articles:write' %}" method='POST'>
  {% csrf_token %} 이렇게 토큰을 넣어준다.
```

