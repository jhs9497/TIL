#### Practice 

1.  user 테이블 전체 데이터를 조회하시오.

```python
User.objects.all()
```

2. id가 19인 사림의 age를 조회하시오.

```python
User.objects.filter(id=19).values('age')
```

3.  모든 사람의 age를 조회하시오.

```python
User.objects.values('age')
```

4. age가 40 이하인 사림들의 id와 balance를 조회하시오. 

```python
User.objects.filter(age__lte=40).values('id', 'balance')
```

5.  last_name이 ‘김’이고 balance가 500 이상인 사람들의 first_name을 조회하시오.

```python
User.objects.filter(balance__gt=500).values('first_name')
```

6. first_name이 ‘수’로 끝나면서 행정구역이 경기도인 사람들의 balance를 조회하시오

```python
User.objects.filter(first_name='수', country='경기도').values('first_name', 'balance')
```















#### HW 1. SQL 용어 및 개념 아래의 보기에서 각 문항

- 테이블 : 열과 행의 모델을 사용해 조직된 데이터 요소들의 집합
- 스키마 : 관계형 데이터베이스에서 구조와 제약조건에 관련한 전반적인 명세를 기술 한 것
- 컬럼 : 고유한 데이터 형식이 지정되는 열
- 레코드 : 단일 구조 데이터 항목을 가리키는 행
- 기본키 : 각 행의 고유값