```python
pip install -U scikit-learn

from sklearn.linear_model import LinearRegression

# 모델 선언
model = LinearRegression()

# x : 데이터, y : 예측 값
model.fit(x_train,y_train)  # fit이 학습한다는 뜻

prediction = model.predict(x_test) # predict
```



- Traning Set : 학습을 위한 데이터 / feature/label이 모두 존재

- Test Set : 모델이 예측하기 위한 데이터 / feature만 존재



## 전처리(pre-processing)

```python
# train/validation 세트 나누기

# 1. 먼저, feature와 label을 정의한다.
# 2. feature / label을 정의했으면, 적절한 비율로 train / validation set을 나눈다.

# 데이터 ~에 따른
feature = [
    'Pclass', 'Sex', 'Age', 'Fare'
]

# 예측 값
labe = [
    'Survived'
]

from sklearn.model_selection import train_test_split

# return 받는 데이터의 순서가 중요합니다.
x_train, x_valid, y_train, y_valid = train_test_split(train[feature], train[label], test_size=0.2, shuffle=True, random_state=30)

# test_size = validation set에 할당한 비율 20%

x_train.shape, y_train.shape, x_valid.shape, y_valid.shape로 확인
```



## 결측치

```python
# 숫자 컬럼

train.infO() 

train.isnull().sum() # 결측치 개수 확인

train['Age'].fillna(0) # Age컬럼의 결측치 다 0으로 채우기

train['Age'].fillna(train['Age'].mean()) # Age컬럼의 결측치 Age평균값으로 채우기

from sklearn.impute import Simpleimputer

imputer = SimpleImputer(strategy='median')
result = imputer.fit_transform(train['Age', 'Pclass'])

# 문자 컬럼
train['Embarked'].fillna('S')

# imputer를 사용하는 경우
imputer = SimpleImputer(strategy='most_frequent')
result = imputer.fit_transform(train[['Embarked', 'Cabin']])
train[['Embarked', 'Cabin']] = result
```

## Label Encoding

문자(categorical)를 수치(numerical)로 변환하는 것

학습을 위해선 모든 문자를 수치로 변환해야 한다.

```python
def convert(data):
    if data == 'Male':
        return 1
    elif data == 'Female':
        return 2
    
train['Sex'].apply(convert)


# sklearn으로 하기 / NaN값 포함되어 있으면 에러남 따라서 결측치 처리 먼저 해주기

from sklearn.preprocessing import LableEncoder

LE = LabelEncoder()
train['Sex'] = LE.fit_transform(train['Sex'])
```



## One Hot Encoding

```python
from sklearn.preprocessing import LabelEncoder

LE = LableEncoder()

train['Embarked'].value_counts()
S 644
C 168
Q 77

# NaN값 처리해주기 / S가 제일 많으니 그냥 S로 넣어주자
train['Embarked'] = train['Embarked'].fillna('S')

# 문자열 -> 숫자열로 바꿔주기
train['Embarked_num'] = LE.fit_transform(train['Embarked']) 

# 잘 바뀌었나 확인
train['Embarked_num'].value_counts()
2   646
0   168
1   77

# 왜 원핫인코딩을 해야하느냐!
# Embarked는 탑승 항구의 이니셜을 나타냈습니다.
# LabelEncoder를 통해서 문자열을 수치형으로 변환해주었습니다.
# 하지만, 이대로 데이터를 기계학습 시키면 'S' = 2 'Q' = 1 로 LableEncoding되어 있는 것을
# Q(1) + Q(1) = S(2) 라고 학습해버림
# 따라서 독립적인 데이터는 별도의 column으로 분리하고, 각각의 컬럼에 해당 값만 True 나머지는 False를 갖게한다. 이것이 원핫인코딩이다.

one_hot = pd.get_dummies(train['Embarked_num'][:6])
one_hot.columns = ['C', 'Q', 'S']

  C Q S
0 0 0 1
1 1 0 0
2 0 0 1
3 0 0 1
4 0 0 1
5 0 1 0

# 요런식으로 나옴!
```



## 정규화

column 간에 다른 min, max 값을 가지는 경우, 정규화를 통해 최소치/최대값의 척도를 맞추어 주는 것

- 네이버 영화평점 (0점~10점) : [2,4,6,8,10]
- 넷플릭스 영화평점 (0점~5점) : [1,2,3,4,5]

위와 같은 경우 사용!

```python
movie = {
    	 'naver': [2,4,6,8,10],
         'netflix': [1,2,3,4,5],
        }

movie = pd.DataFrame(data=movie)

from sklearn.preprocessing import MinMaxScaler

min_max_scaler = MinMaxScaler()

min_max_movie = min_max_sclaer.fit_transform(movie)

pd.DataFrame(min_max_movie, columns=['naver', 'netflix'])

# 정규화를 통해 두 플랫폼의 영화 평점 모두 0~1점 사이에 분포하도록 함

    naver    netflix
0   0.00      0.00
1   0.25      0.25
2   0.50      0.50
3   0.75      0.75
4   1.00      1.00
```



## 표준화

평균이 0, 표준편차가 1이 되도록 변환

```python
from sklearn.preprocessing import StandardScaler

standard_scaler = StandardScaler()

x = np.arange(10)
# outlier 추가
x[9] = 1000

# 그냥 뽑으면 outlier때문에 이상해짐

x.mean() = 103.6
x.std() = 298.xxxxxx

# 그래서 StandardScaler 사용

scaled = standard_scaler.fit_transfomr(x.reshape(-1, 1))

scaled.mean() = 4.xxx
scaled.std() = 1.0
```



## 분류_데이터셋 활용

```python
# iris 데이터 셋 불러오기

DESCR : 데이터셋의 정보
data : feature data
feature_names : feature data의 컬럼 이름
target : label data (수치형)
target_names : label의 이름 (문자형)

from sklearn.datasets import load_iris

iris = load_iris()

data = iris['data']
feature_names = iris['feature_names']
target = iris['target']

```



## 데이터프레임 만들기

```python
df_iris = pd.DataFrame(data, columns=feature_names)
```



## 로지스틱 회귀

```python
from sklearn.linear_model import LogisticRegression

# 선형관계에서 분류를 적용하여 발생 가능성을 예측하는데 사용됨

# 모델 선언
model = LogisticRegression()

# 모델 학습
model.fit(x_train, y_train)

print(model) 하면 세팅값 설정을 볼 수 있음

# 예측 
prediction = model.predict(x_valid)

# 정확도 알아보기
(prediction == y_valid).mean()
```

