```python
# 제일 큰 수와 두 번째 큰 수만 가지고 노는 문제

n, m, k = map(int, input().split())

data_list = list(map(int, input().split()))

# 제일 큰 수를 뽑자

Max = max(data_list)  # 제일 큰 수

# 제일 큰 수의 인덱스와 두번째로 큰 수(혹은 제일 큰 수가 2개 이상일수도)의 인덱스를 뽑자

Max_index = 0

# data_list를 돌면서 (range로)
for i in range(len(data_list)):
    # 만약 data_list의 i 인덱싱이 Max와 같다면
    if data_list[i] == Max:
        # Max_index에 그 인덱스값 더하고 BREAK! 
        Max_index += i
        break
        
# 초기의 data_list에서 뽑힌 그 인덱싱에 해당하는 값은 지워준다         
data_list.pop(Max_index)

Second = max(data_list)  # 두 번째로 큰 수


K_list = []

for i in range(1, 1000):
    K_list.append(i*(k+1) -1) # 두 번째로 큰 수가 나와야할 자리

total = 0

for j in range(m):
    if j in K_list:
        total += Second
    else:
        total += Max
print(total)
```

