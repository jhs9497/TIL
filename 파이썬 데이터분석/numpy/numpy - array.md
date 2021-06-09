## numpy - array

```python
import numpy as np

arr = np.array([1, 2, 3, 4], dtype=int)

print(arr, arr.shape, type(arr))

mylist = [[1,2,3,4], [7,8,9,0]]

arr2 = np.array(mylist)

print(arr2, arr2.shape, type(arr2))

# arr은 데이터타입이 단일이어야 한다 
# 걍 타입을 바꿔버림 ex) int랑 str 혼재되어 있고 dtype 지정 안하면 int를 자동으로 str로 바꿈

#아래와 같은 경우 그냥 정수화 되어버림
arr3 = np.array([1,2,3,4,3.14], dtype=int)
```



## numpy - slice

```python
# 1차원 arr일 경우
arr = np.array([0,1,2,3,4,5,6,7,8,9,10])

print(arr[2])
# 2출력

print(arr[-1])
# 맨 마지막 10 출력

print(arr[-3])
# 8 출력

# print(arr[11])
# 범위 넘어가서 에러


# 2차원 arr일 경우
arr2 = np.array([[1,2,3,4],
								 [5,6,7,8],
								 [9,10,11,12]])

print(arr2[0,3])
# 4출력

# 슬라이싱
# row(행)을 모두 가져오려는 경우
print(arr2[0, :])  # 0번째 로우 가져오고, 행은 모두 가져오라는 뜻

# column(열)을 모두 가져오려는 경우
print(arr2[:, 2]) # 로우는 다 가져오고, 2번째 행을 가져오라는 뜻

# 부분적으로 가져오려는 경우
print(arr2[:2, :]) # 로우는 0,1 가져오고 행은 다 가져오라는 뜻

print(arr2[:2, 2:]) # 로우는 0,1 가져오고 행도 0,1까지만 가져오라는 뜻
```



## numpy - fancy 인덱싱

```python
arr = np.array([10,2,3,4,5,6,7,8,9,10])

print(arr[[1,3,5]]) # 1,3,5번째 요소를 가져와라
```



## boolean indexing

```python
arr = np.array([1,2,3,4,5,6])

myTrueFalse = [True, True, True, False, False, True]  # 위에 arr의 갯수와 맞춰서 T/F 정해주고

print(arr[myTrueFalse])
#1,2,3,6만 출력됨


arr2 = np.array([[1,2,3,4],
								 [5,6,7,8],
								 [9,10,11,12]])

# 조건필터

print(arr2 > 3) # arr2중에 3 초과인 친구들만 boolean index로 뽑아줘

# [[False False False True]
#  [True True True True]
#  [True True True True]
#  [True True True True]] 요렇게 출력됨

print(arr2[arr2 > 2]) # 위 친구를 index로 활용해서 2 초과인 친구 출력가능
```

