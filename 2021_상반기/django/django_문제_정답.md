#### 1번 문제

> 정답 : as_table()
>
> as_p() : 각 필드가 단락(paragraph)으로 렌더링
>
> as_ul() : 각 필드가 목록항목(list item)으로 렌더링
>
> as_table() : 각 필드가 테이블 행으로 렌더링



#### 2번 문제

> request로 받은 data가 'POST'이지만 forms.py에서 정의한 양식에 위배되는 경우 return할 공간을 찾지 못하게 되어 함수를 벗어나지 못한다. 그러므로 context이하 문을 if/else 바깥쪽으로 빼서 data의 양식이 위배된 경우 설정한 data를 'form'에 담아서 return할 수 있도록 유도한다.



#### 3번 문제

>ㅇForm
>
>어떤 모델에 저장해야 하는지 알 수 없기 때문에 유효성 검사를 하고 실제로 DB에 저장할 때는  cleaned_data 와 article = Article(title=title, content=content) 를 사용해서 따로 .save() 를 해야 한다.
>Form Class가 cleaned_data 로 딕셔너리로 만들어서 제공해 주고, 우리는 .get 으로 가져와서 Article 을 만드는데 사용한다.
>
>
>
>
>ㅇModelForm
>
>django 가 해당 모델에서 양식에 필요한 대부분의 정보를 이미 정의한다.
>
>forms.py 에 Meta 정보로 models.py 에 이미 정의한  Article 을 넘겼기 때문에 어떤 모델에 레코드를 만들어야 할지 알고 있어서 바로 .save() 가 가능하다.



#### 4번 문제

> instance=article
>
> update함수의 경우 기존에 생성했던 정보를 우선적으로 가져와서 사용자에게 보여줘야 하는데 instance인자는 수정 대상이 되는 객체를 지정하는 역할을 한다. 사용자에게 수정 대상이 되는 객체는 위에서 정의한 article  (article = Article.objects.get(pk=pk)) 에 해당하므로 article을 instance에 담아서 form에 담아준다.



#### 5번 문제

>@require_http_methods(['GET', 'POST'])