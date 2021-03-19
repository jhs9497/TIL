### 06_django_homework



#### 1. static 파일 기본 설정

```python
STATIC_URL = '/static/'

STATICFILES_DIRS= [
    # crud/static/stylesheets/style.css
    BASE_DIR / 'crud' / 'static',
]

# 모든 스태틱 파일들을 이 폴더에 모아줘
STATIC_ROOT = BASE_DIR / 'staticfiles'

django.contirb.staticfiles,
```



#### 2. media 파일 기본 설정

```python
# MEDIA_URL
# 업로드된 파일의 주소를 만들어줌.
MEDIA_URL = '/uploaded_files/'

# MEDIA_ROOT
# 실제 업로드되는 파일이 저장되는 경로 
MEDIA_ROOT = BASE_DIR / 'uploaded_files'
```



#### 3. Serving files uploaded by user during development

```python
from django.conf import settings
from django.conf.urls.static import static

+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```



---



### 06_django_workshop



##### 1.태그를 사용할 경우 반드시 사용해야 하는 enctype 속성 값 (a)를 작성하시오.

```python
enctype="multipart/form-data"
```



##### 2.  accept 속성은 파일 업로드 제어에서 선택할 수 있는 파일 유형을 정의하는 속성이 며 input 태그의 type이 file일 경우에만 유효하다. 예를 들어 표준 비디오 형식 뿐만 아니라 PDF 파일도 받을 수 있어야 할 때, 빈칸 (b)에 들어갈 알맞은 속성 값을 작성하시오.

```python
all
```



---



### 07_django_homework



#### 1. Compiled Bootstrap

1.  프로젝트네임폴더 안에 staticfiles 폴더를 만들고 그 안에  stylesheets폴더를 만든다.
2.  stylesheets 폴더 안에 style.css ( 보통 이렇게 이름 짓는다.) 를 만들고 원하는 style을 작성한다.
3. setting.py에 들어가서 아래와 같이 코드를 작성한다.

```python
STATIC_URL = '/static/'

STATICFILES_DIRS= [
    # crud/static/stylesheets/style.css
    BASE_DIR / 'crud' / 'static',
]
```

4. css를 적용하고 싶은 html파일로 가서 아래와 같이 코드를 작성한다.

```html
{% load static %}

{% block css %}
<link rel="stylesheet" href="{% static 'stylesheets/style.css' %}">
{% endblock %}
```



---



### 07_django_workshop



