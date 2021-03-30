#### 1. Lookup

- exact : 정확히 일치하는 경우만을 가져온다
- contains:  대소문자를 구분해서 ' abcde ' 가 들어있는 경우를 가져온다.
- gt: id값등에서 ~~보다 큰 값을 가져온다.



#### 2.  1:N 관계 설정

- CASCADE: 이 글의 작성자가 데이터베이스에서 삭제 되었을 때 이 글도 같이 삭제한다.
- PROTECT: 이 글의 작성자가 삭제되어도 글은 삭제하지 않는다
- SET_NULL: 공백이 TRUE일 경우에만 글의 작성자를 공란으로 두고 글은 삭제하지 않는다(?)
- SET_DEFAULT: 디폴트값이 정의되어 있는 경우에, 글의 작성자를 디폴트값으로 바꾸고 글은 삭제하지 않는다.



#### 3.  comment create view

- commit=False: 실제 DB에 저장을 하지는 않지만, form에 담긴 인스턴스를 반환하여 사용할 수 있게 한다. 바로 저장을 하게 되면 오류가 난다. 왜냐하면 현재 article정보가 빠져있기 때문이다 스키마에는 article정보까지 들어가야 하는데 빠져있으므로 오류가 난다.



#### 4.  1:N DB API

- comments


