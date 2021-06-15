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
```

