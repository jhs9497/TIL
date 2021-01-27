## 1. 평균 점수 구하기

key 값으로 과목명, value 값으로 점수를 가지는 dictionary를 전달 받아, 전체 과목의 평균 점수를 반환하는 함수 get_dict_avg 함수를 작성하시오.

In [23]:

```
def get_dict_avg(x):
    total = 0
    for i in x.values():
        total += i
    return total / len(x)
        
        
        
get_dict_avg({
    'python' : 80,
    'algorithm' : 90,
    'django' : 89,
    'web' : 83,
})
```

Out[23]:

```
85.5
```

### #### 