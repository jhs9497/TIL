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

