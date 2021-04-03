# SQL and SQL with ORM



#### 1. (a) 는 관계형 데이터베이스 관리시스템의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어이다. (a)에 들어갈 단어로 적합한 것은 ?

1.  ORM
2.  SQL
3.  IBM
4. Database



#### 2. a, b 빈 칸을 채우시오

```
SQL은 (___a___)를 만나기 전까지 절대 실행되지 않습니다. 따라서 들여쓰기를 비교적 자유롭게 할 수 있습니다. (___b___)로 시작하는 모든 명령어는 SQLite에서 데이터베이스를 조금 더 편리하게 다루기 위해 제공하는 명령어이며, SQL 문법에 속하지 않습니다.
```



#### 3.  SQL에서 테이블을 생성하려 할 때 빈 칸에 들어갈 명령어를 작성하시오

```sql
(____a_____) (
	id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INT NOT NULL,
  ...
);
```



#### 4. SQL에서 테이블을 제거하려 할 때 빈 칸에 들어갈 명령어를 작성하시오

```sql
sqlite> (____a_____) classmates;
sqlite> .tables // 테이블 제거 확인
```



#### 5. 전체 데이터를 조회 하고 싶을 때 사용하는 명령어를 SQL과 django ORM상에서의 SQL 명령어 두 가지를 모두 작성하시오

1. SQL :
2. SQL with django :



#### 6. 해당 레코드를 수정하려할 때 빈 칸을 채우시오.

- ORM: `101` 번 유저의 `last_name` 을 '김' 으로 수정
- SQL: `101` 번 유저의 `first_name` 을 '철수' 로 수정



```python
# orm

user = User.objects.(__a__)
user.last_name = '김'
(__b__)

```



```sql
-- sql

UPDATE users_user
(__c__) first_name='철수'
(__d__) id=101;

```



#### 7. 나이가 30이면서 성이 김씨인 사람의 인원 수를 조회하고자 할 때 빈 칸을 채우시오

```python
# orm

User.objects.(__a__)(age=30, last_name='김').count()
```



```sql
-- sql

SELECT (__b__)(*)
FROM users_user
WHERE age=30 AND last_name='김';
```



#### 8. 나이가 많은 사람순으로 10명만 조회하고자 할 때 빈 칸을 채우시오



```python
# orm

User.objects.order_by('-age')(__a__)
```



```sql
SELECT *
FROM users_user
ORDER BY age (__b__)
(__c__) 10;
```

































## 정답

1. 2번

2.  a = ;  b =  .

3.  CREATE TABLE table

4.  DROP TABLE

5.  SQL : SELECT * FROM table;    

    SQL with django : User.objects.all()

6.  (a)  : get(pk=101)  (b) : user.save() 
    (c) : SET   (d)  : WHERE

7.  (a) : filter    (b) : COUNT

8.  (a) : [:10]   (b) : DESC  (c) :  LIMIT

