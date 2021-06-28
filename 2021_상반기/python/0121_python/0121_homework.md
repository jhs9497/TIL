## 1번 문제

LEGB

Local scope

enclosed scope

global scope

built-in scope



## 2번 문제

1번 

1번이 어디가 확실히 틀린지는 모르겠지만 나머지 보기들이 정확히 맞다고 생각합니다



## 3번 문제

재귀함수는 자기 자신을 이용하여 함수를 설정하기 때문에 설정해야 하는 변수의 가짓수가 반복문에 비해 비교적 적은 장점이 있다. 하지만 함수 속에서 함수가 실행되는 작업이 지속되기 때문에 반복문 보다 처리 속도가 느리다는 단점이 있다.



## 4번 문제

```python
def get_secret_word(args):
    word = ''
    for i in args :
        aski = chr(i)
        word += aski
        
        
    return word
```





### 5번 문제

```python
def get_secret_number(numbers):
    total = 0
    for number in numbers:
        total += ord(number)
        
    return total
```





### 6번 문제

```python
def get_strong_word(x, y):
    def get_secret_number(numbers):
        X_total = 0
        Y_total = 0
        for x in numbers:
            X_total += ord(x)
        for y in numbers:
            Y_total += ord(y)
            
    if X_total > Y_total:
        return X_total
        
    elif X_total == Y_total:
        print('값이 같습니다')
    else:
        return Y_total
```

