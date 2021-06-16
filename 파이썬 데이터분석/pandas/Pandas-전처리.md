## 빈 값 채우기

```python
df['키'].fillna(-1)

# '키'컬럼에 비어있는 값을 -1로 채워줘! but 이건 원본 수정은 안됨

df['키'].fillna(-1, inplace=True)
# 원본까지 수정

df['키'] = df['키'].fillna(-1) 
# 요렇게도 원본까지 수정 가능

height = df['키'].mean()
df['키'] = df['키'].fillna(height)
# 빈값에 키의 평균값을 넣어줘
```



## 빈 값 제거

```python
df.dropna()
# 빈 값이 있는 행을 지워준다.

df.dropna(axis=0)
# 빈 값이 있는 행을 지워준다.

df.dropna(axis=1)
# 빈 값이 있는 열을 지워준다.

df.dropna(axis=0, how='all')
# 행 전체가 NaN값일 경우에만 날려라
```



## 중복값 제거

```python
df['키'].drop_duplicates()
# 키 컬럼에서 중복된 값은 지워줘 (처음 나온 값이 남음)

df['키'].drop_duplicates(keep='last')
# 키 컬럼에서 중복된 값은 지워줘 (나중에 나온 값이 남음)

df.drop_duplicates('그룹')
# 그룹행전체에 중복된 값은 지워줘
```



## 행/열 제거

```python
df.drop('그룹', axis=1)
# 컬럼(열) 제거하기

df.drop(3, axis=0)
# 행(인덱스로) 제거하기
```



## 데이터프레임 합치기

```python
df_concat = pd.concat([df, df_copy], sort=False)
# row기준으로 합치기 (밑으로 붙히기), concat+[합칠 데이터프레임 리스트형식으로], sort=False

df_concat.reset_index(drop=True)
# 인덱스가 뒤죽박죽되어 있어서 새로 정리

df_concat = pd.concat([df, df_copy], axis=1)
# column기준으로 합치기 (옆으로 붙히기)
```



## 데이터프레임 병합하기

```python
# 단순 합치기와는 다르게 특정 고유 키값을 기준으로 병학하기(merge)


# 이름을 기준으로 두 DataFrame을 병합하기
pd.merge(df, df_right, on='이름', how='left')
# 'left'옵션을 부여하면, left DataFrame에 키 값이 존재하면 해당 데이터를 유지하고, 병합한 right DataFrame의 값은 NaN이 대입 된다. (left 기준으로 merge한다는 뜻 -> left친구들은 다 살림!)

pd.merge(df, df_right, on='이름', how='inner')
# 교집합

pd.merge(df, df_right, on='이름', how='outer')
# 합집합
```



## Series(열) Type 관리하기

```python
object : 일반 문자열 타입
float : 실수
int : 정수
category : 카테고리
datetime : 시간

df['키'].dtype
# 키 컬럼의 type확인
    
df['키'].astype(int)
# 키 컬럼을 정수형으로 변환한다.

df['생년월일'] = pd.to_datetime(df['생년월일'])
# 날짜는 독특하게 to_datetime이라는 방식으로 컬럼 type을 변환해야 한다

# why? 월, 일, 요일 등등 날짜 정보를 세부적으로 추출할 수 있게 하기 위해서
df['생년월일'].dt.year
# 연도만 뽑혀 나옴! 이 밖에도 .month .day .hour .minute .second .dayofweek .dayofyear
```



## apply 함수

```python
# 남자는 1, 여자는 0으로 바꿔주고 싶을 때

df.loc[df['성별'] == '남자', '성별'] = 1
df.loc[df['성별'] == '여자', '성별'] = 0

def male_or_female(x):
    if x == '남자':
        return 1
    elif x == '여자':
        return 0
    
def['성별_NEW'] = df['성별'].apply(male_or_female)


# 데이터 프레임 전체를 넘겨줄 때
def cm_to_brand(df):
    value = df['브랜드평판지수'] / df['키']
    return value

df.apply(cm_to_brand, axis=1)
```



## lamda 함수

```python
# lamda는 1줄로 작성하는 간단 함수식이다

df['성별'].apply(lambda x: 1 if x =='남자' else 0)

df['키/2'] = df['키'].apply(lambda x: x / 2)
# 키컬럼의 키를 다 2로 나눈다
```



## Map 함수

```python
my_map = {
    '남자' : 1,
    '여자' : 0
}

df['성별_NEW'] = df['성별'].map(my_map)
```



## Select_dtypes 함수

```python
df.select_dtypes(include='object').columns
# 문자열이 있는 column만 선택

df.select_dtypes(exclude='object')
# 문자열이 없는 column만 선택
```



## One-hot-encoding

```python
원핫인코딩은 한개의 요소는 True 그리고 나머지 요소들은 False로 만들어주는 기법이다.
추후 머신러닝 알고리즘 발전을 위하여 알아둬야함!

pd.get_dummies(df['혈액형_code'], prefix='혈액형')
```