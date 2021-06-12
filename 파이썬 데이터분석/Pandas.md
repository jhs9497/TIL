## Pandas

데이터분석을 위한 패키지



## Sereis와 DataFrame

Series : 1차원으로 이루어진 데이터 배열

DataFrame : Series가 모여서 2차원으로 이루어진 데이터 배열

```python
# Series 만들기
print(pd.Series([1,2,3,4]))

#왼쪽은 인덱스, 오른쪽은 값
#> 0    1
#  1    2
#  2    3
#  3    4
#dtype: int64

# DataFrame 만들기 
# 1) 리스트형식으로 만들기
company = [['삼성', 2000, '스마트폰'],
		   ['현대', 1000, '자동차'],
		   ['네이버', 500, 'IT']
	      ]

df1 = pd.DataFrame(company)
print(df1)

#     0     1     2
# 0   삼성  2000  스마트폰
# 1   현대  1000   자동차
# 2  네이버   500    IT

# 제목 컬럼 만들기
df1.columns = ['기업명', '매출액', '업종']
print(df1)
#   기업명   매출액    업종
# 0   삼성  2000  스마트폰
# 1   현대  1000   자동차
# 2  네이버   500    IT


# 2) Dict형식으로 만들기
company2 = {'기업명': ['삼성', '현대', '네이버'],
			'매출액': [2000, 1000, 500],
			'업종': ['스마트폰', '자동차', 'IT']
		   }

df2 = pd.DataFrame(company2)
print(df2)

#   기업명   매출액    업종
# 0   삼성  2000  스마트폰
# 1   현대  1000   자동차
# 2  네이버   500    IT


# 해당 컬럼(Sereis)만 뽑기
print(df2['기업명'], type(df2['기업명']))

# 0     삼성
# 1     현대
# 2    네이버
# Name: 기업명, dtype: object <class 'pandas.core.series.Series'>
```



## 통계값 다루기

```python
#최솟값
.min()

#최댓값
.max()

#합계
.sum()

#평균
.mean()

#표준편차
.std()
dataset = pd.read_csv('data/mtcars.csv')
print(dataset['disp'].std())
# 123.93869383138194

# 분산
.var()

# 갯수 세기
.count()

# 중앙값
.median()

# 최빈값
.mode()
```



## PivotTable

- 엑셀의 피벗테이블과 동일하다
- 데이터 열 중에서 두 개의 열을 각각 행 인덱스, 열 인덱스로 사용하여 데이터를 조회하여 펼쳐놓은 것을 의미한다.
- 왼쪽에 나타나는 인덱스를 행 인덱스, 상단에 나타나는 인덱스를 열 인덱스라고 부른다.

```python

```



## GroupBy(그룹으로 묶어 보기)

```python
dataset.groupby('disp')['disp'].mean()
```





## 예제 1번

```python
import pandas as pd
import numpy

dataset = pd.read_csv('data/mtcars.csv')

# qesc라는 변수에 qesc컬럼을 저장하고
qesc = dataset['qsec']

# qesc중 가장 큰 값
qesc_max = qesc.max()
# qesc중 가장 작은 값
qesc_min = qesc.min()

# min-max 스케일링은 각 값들을 0~1 사이에 분포하도록 조정하는 것
# 각 값들에서 최소값을 뺀 값 / 최대값 - 최소값 이므로
# for문 안돌려도 알아서 해줌...
minmax = (qesc - qesc_min) / (qesc_max - qesc_min)

# 이 중에 0.5 이상인 것의 count를 세면 된다.
print(minmax[minmax>0.5].count())
```

