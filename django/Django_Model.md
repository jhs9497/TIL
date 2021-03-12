# Django Model

### 순서

```
 M - U - V - T

-1. 프로젝트를 만들고, 앱을 만들고
프로젝트 settings에서 만든 앱을 추가시켜주고, 바로 밑에 'django_extensions'  추가
-2. 내가 만든 앱 폴더에 있는 Model로 가서, 
class Article(models.Model): 클래스를 생성, Article, 이름은 내 맘대로 정해도 됨.
내가 원하는, 도구(?)를 설정해서 넣어준다 
ex) 제목, 내용 , 만든시간, 업데이트 시간 등을 추가.
  title = models.CharField(max_length=10) # 맥스렝스가 길이 제한
  content = models.TextField() #길이 제한 없음
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
                #auto_now에 add를 넣으면, 갱신이 안됨, 추가가 됨.
                #add가 없으면, 값을 수정할때 마다, 갱신이 됨.
                
 ===================================================================================
 이제 뼈대(?)는 다 만들었으니, 추가
python manage.py makemigrations 를 통해 추가를 해주고
python manage.py migrate 를 해주고, 
python manage.py showmigrations로 확인을 해주고
python manage.py shell_plus 를 해주면 ,이제 터미널 창에서, 
							파이썬 처럼, 주피터처럼 입력, 출력이 됨 
							
```



### CRUD

```
Create
1. article = Article() article이라는 변수에, 클래스를 넣어주어, article만 출력하면
 <Article: Article object (None)> 라고 뜸 none이라고 뜨는 이유는 인스턴스가 비어있다..
 article.save() 이렇게 저장을 해주고
 다시출력하면,
 article (출력)
 <Article: Article object (1)> 생성됨.
 sqlite로 확인하면 id=1값에 저장이 된 것을 확인.
 
2. id=1에 있는 값을 수정 혹은 추가
 1)article.title = 'first article' 이렇게 바꾸고 세이브
   article.content = 'first content' 이렇게 바꾸고 세이브 
   
 2) article2라는 인스턴스를 만들면서, 바로
  article2 = Article(title = 'second title', content = 'second content')
  article2.save()
 
 3) article3이라는 인스턴트를 만들면서, 
 	article3 = Article.objects.create(title = 'third title', content = 'third content')
 	추가적인 저장은 필요없음. 여기서 Article은 class를 의미함.

```



### 데이터 가져오기

```
1. 모든 데이터를 가져오겠다
  article_list = Article.objects.all() 이렇게하고
  article_list를 출력하면, 
  <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]> 
  이렇게 쿼리셋이라는 유사 리스트를 만들어냄 
  인덱싱 가능, 슬라이싱 가능 등등 파이썬의 리스트처럼 사용이 가능하지만 리스트는 아님
  파이썬의 리스트의 기능을 거의 다 할 수 있는데 안되는것도 있음(안되는건 뭔지 모름 아직)
  
2.하나만 가져오겠다
 first_article = Article.objects.get(id = 1) -- id =1 인 값만 가져오게됨
 first_article = Article.objects.get('존재하는 내용')  
 존재하는 내용이 있으면, 가져오고 없으면 에러 뜸
 
 '존재하는 내용으로', 겟으로 가져오면, <Article: Article object (1)> 이런식으로 가져온다
 근데 겟으로 가져오면 쿼리셋이 아니다. 
 
 
 3. 필터로 가져오면, 쿼리셋으로 가져온다.
 
  second_article = Article.objects.filter(id=2) 
 second_article 출력을 해보면,
 <QuerySet [<Article: Article object (2)>]>
 second_article.title 이렇게 하면 오류가 뜸 
 second_article[0].title 이렇게 꺼내와야 꺼내 짐. 타이틀 값이.
 
 필터로 아이디가 없는 값을 뽑으려고 한다면, 빈 쿼리셋이 있다고 뜸 에러가 뜨진 않음.
```



### 지우기

```
먼저 자료를 가져와야함.
변수로(?) 가져오고 , 지우면 됨.

1) article1 = Article.objects.get(id=1) 
  가져오고
  article1.delete() 하면 id=1은 지워짐

2) 가져오면서 바로 지우는 법
   Article.objects.get(id=2).delete()
```



- GET - 정보를 보여줘
- POST - 정보를 처리해줘(저장)
- PUT / Patch - 정보를 수정해줘
- DELETE - 정보를 삭제해줘





























