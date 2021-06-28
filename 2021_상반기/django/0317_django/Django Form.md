### Django Form

---

>1. modle정보에 맞게 HTML 코드를 손쉽게 생성해준다.
>
>2. 유효성 검사
>   - is_valid()



#### 1. Form

> 내가 직접 만든 Django Form



#### 2. ModelForm

> Model 정보가 바인딩 되어있는 Django Form

```python
forms.py

from django.db import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content')
        # 또는 fields = '__all__' <- 다가져오기
```

