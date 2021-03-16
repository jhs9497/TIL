# Django form 시스템의 핵심은 재사용과 유효성 검사입니다.
# 1. 재사용 가능한 HTML Form을 자동으로 만들어줍니다.
# 2. Form에 담긴 데이터(사용자 입력값)을 알아서 검증해줍니다.

from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    '''
    field: 실제 HTML input태그의 데이터 타입을 지정
    widget: 실제 HTML input태그의 모습

    ModelForm은 이미 정의한 Model을 이용하여
    Forms 시스템을 더욱 쉽게 사용하게 해주는 기능입니다.
    '''
    title = forms.CharField(
        lable='제목',
        widget=forms.TextInput(
            attrs={
                'class':'my-title',
                'placeholder':'제목을 입력해주세요~!',
            }
        )
    )

    class Meta:
        model = Article  # 어떤 모델인지 명시
        fields = ('title', 'content') # 위에 작성한 모델(클래스)의 필드 중에서 보여줄것만 작성
        # 튜플형태라 하나만 적으려면 ('title',) 이렇게 적어야함!
        # fields = '__all__' # 다 보여줘!
    