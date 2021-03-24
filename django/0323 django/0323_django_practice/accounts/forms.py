from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model() # 활성화 유저 모델

class CustomUserCreationForm(UserCreationForm):
    '''
    UserCreationForm을 커스터마이징 하는 이유는
    UserCreationForm이 django 내장 User모델을 가리키기 때문입니다.
    '''
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)
        #        username, password, password_confirm + email 추가

class CustomUserChangeForm(UserChangeForm):
    password = None 
    
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')