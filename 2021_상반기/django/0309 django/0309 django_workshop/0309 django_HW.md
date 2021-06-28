### 1. MTV 

Django는 MTV 디자인 패턴으로 이루어진 Web Framework이다. 여기서 MTV는 무엇의 약자이며 각각 MVC 디자인 패턴과 어떻게 매칭이 되며 각 키워드가 django에서 하는 역할을 간략히 서술하시오.

일반적인MTV-장고의 MVC

- Model-Model -> 데이터베이스관리

- Template-View -> 인터페이스 또는 화면 담당

- View-COntroller: Model과 Template 사이의 중개자
  -  HTTP 요청을 수신하고 HTTP 응답을 반환
  - Model을 통해 요청을 충족시키는데 필요한 데이터에 접근
  - 그리고 템플릿에게 응답의 서식 설정을 맡김



### 2. URL

- variable routing



### 3. Django template path

- templates



### 4. Static web and Dynamic web

> 미리만들어진 것 vs 사용자가 요청했을 때 만들어지는 페이지

- static web
  - 사용자의 요청에 따라 서버 안에 이미 저장되어 있는 문서 자체를 사용자에게 보여준다.
- dynamic web
  - 사용자의 요청이 들어오면 web application 서버에서 상황에 맞는 문서를 생성해 제공한다.





