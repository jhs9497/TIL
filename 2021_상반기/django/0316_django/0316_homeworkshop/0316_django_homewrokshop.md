#### homework

##### 1. 왜 변수 context는 if else 구문과 동일한 레벨에 작성 되어있는가?

>request에서 넘어온 method가 POST가 아닌경우 빈 값을 articles/creat.html에 보내야 하기 때문이다



#####  2. 왜 request의 http method는 POST 먼저 확인하도록 작성하는가?

> django에서 request에 쓸 수 있는 method가 몇가지 있는데 그 중에서 'POST' method만 수정이 가능하게 데이터를 보내는 method이기 때문이다. 즉 POST인지 아닌지가 중요하기 때문에 POST를 먼저 확인하는 것이 효율적이다.
>
> GET부터 확인하면 GET 이외에 것들이 모두 DB에 영향을 줌 그럼 아니됨!



#### workshop

##### 1. 모델 폼을 정의하기 위해 빈칸에 들어갈 코드를 작성하시오.

```django
forms.ModelForm
```



##### 2.  글 작성 기능을 구현하기 위해 다음과 같이 코드를 작성하였다. 서버를 실행시킨 후 기능을 테스트 해보니 특정 상황에서 문제가 발생하였다. 이유와 해결방법을 작성하시오.

> context 이하 구문이 else: 안에 들어가있어서 문제가 생긴 것 같다. 만약 전해받은 데이터의 method가 'POST'이지만 forms.py에 정의한 조건에 부합하지 않은 경우 return해서 나올 조건이 없다. 그러므로 context이하를 if, else와 동일하게 만들면서 1) method가 'POST'이지만 조건에 부합하지 않는 경우는 django에서 미리 세팅해놓은 에러값을 form에 저장해서 context로 reservations/create.html에 보내도록 하고 2) method가 'POST'가 아닌 경우, 빈 값을 form에 정의하고 context에 아무것도 담지 않은 채 reservations/creat.html로 보내도록 만든다.



##### 3. 글 수정 기능을 구현하기 위해 빈칸에 들어갈 코드를 작성하시오.

```django
a) form = ReservationForm(request.POST)
b) form = ReservationForm(instance=reservation)
```



##### 4. 글 수정 기능을 구현하기 위해 빈칸에 들어갈 수 있는 코드를 모두 작성하시오

```django
form.as_p

form.title
form.content  ? ? 근데 workshop에는 뭐로 정의했는지 모르겠음
```

