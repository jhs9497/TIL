## DBMS의 PK와 INDEX

- INDEX의 장점

  - 테이블을 조회하는 속도 & 성능 향상
  - 시스템의 부하를 줄일 수 있다.
  - 원하는 데이터를 빠르게 찾을 수 있다.

- INDEX의 단점

  - DB 저장 공간을 차지한다. (꽤 큰 용량을 잡아먹는다.)
  - 인덱스를 관리하기 위한 작업이 필요하다.
  - 잘못 사용할 경우 오히려 성능이 저하된다.

- INDEX를 활용하면 안 좋은 경우

  - DELETE, UPDATE 등 컬럼의 변동이 자주 일어나는 경우

  

##### PK를 생성하면 INDEX가 생성되고, PK를 삭제하면 INDEX가 삭제된다!

- PK
  - Primary Key, 데이터를 구별할 수 있는 고유한 값
- INDEX 
  - 데이터베이스 테이블의 검색 속도를 향상시키기 위한 자료구조
  - Indexes Table이라고 한다. 즉 Index도 테이블의 한 종류이다. (데이터 베이스 객체의 한 종류)
    - 데이터 베이스 객체란 ?
      - 데이터베이스 내에 존재하는 논리적인 저장 구조
      - Table, View, Indexes, synonym, sequence 등
      - DDL문(CREATE, ALTER, DROP, TRUNCATE)으로 생성, 수정, 삭제가 가능하다.
  - PK가 아닌 컬럼이라도 INDEX를 생성할 수 있다.

##### 



## INDEX의 동작

- INDEX를 잘 쓰려면 ?
  - Where 조건 작성시 Index를 적용할 수 있는 컬럼 조건을 상단에 작성한다.
  - Index로 사용된 컬럼은 컬럼값 그대로 사용해야한다.
    - Where Age > 18 (Index 적용) 
    - Where Age *2  > 36 (연산 적용하면 Index 적용 불가)
  - Between, like, >, < 등 범위 조건 뒤의 Index들은 적용되지 않으니 가장 마지막에 활용한다.
    - Where Id = '8' and Age > 16 (Index 적용)
    - Where Age > 16 (Index 적용) and Id = '8' (Index 적용 불가)



