### gravity 문제

#### Think Proccss ⚡

1. 꼭대기만 생각하면 되지 않을까
2. 굳이 오른쪽 90도 돌리지 말고 빌딩들을 오른쪽으로 쭉 민다고 생각하자.
3. 인덱싱으로 설정한 빌딩이 오른쪽으로 1칸 이동할때마다 카운트에 추가하자.

#### 코딩풀이 👀

```python
A = [7, 4, 2, 0, 0, 6, 0, 7, 0] # 예시로 나온 건물을 리스트에 층 감안해서 정렬

answer = 0
for i in range(len(A)-1): # 0~8 9번을 돌린다   # i = 0  7층짜리가 먼저 선정
    count = 0 # 오른쪽으로 움직이는 만큼 추가한다.
    for j in range(i+1, len(A)): # i= 1부터 뒤까지 비교하려고 1~9까지 1~8번째
        if A[i] > A[j]: # 만약 꼭대기가 오른쪽 애보다 크면 오른쪽으로 움직일 수 있다.
            count += 1
            if answer < count:
                answer = count
print(answer)

# 뭔가 많은 test_case에 넣으면 실패할거 같다.
```

#### 원본코드🤞

```python
A = [7, 4, 2, 0, 0, 6, 0, 7, 0]

answer = 0
for i in range(len(A)-1): # 0~8 9번을 돌린다   # i = 0  7층짜리가 먼저 선정
    count = 0
    for j in range(i+1, len(A)): # i= 1부터 뒤까지 비교하려고 1~9까지 1~8번째
        if A[i] > A[j]:
            count += 1
            if answer < count:
                answer = count
print(answer)
```



***



### babygin 찾기 문제

#### Think Process⚡

1. 해당 리스트를 우선 숫자가 몇 개씩 있는지 세보자.
2.  [0, 1,  2,  0, 0, 0, 0, 3, 1, 2] 요런식
3. 만약 저 리스트에 3이상이 들어있으면 어느 한 숫자가 3개이상 있다는 거니깐 triplet 조건충족
4. 연속된 3개의 숫자가 같으면 나머지 조건도 충족
5. 찾았다 babygin~

#### 코딩풀이👀

```python

number = list(map(int, input().split()))

count_number = [0]*10 # 0~9까지 몇 개씩 있나 세야하니깐 0이 내용물인 10칸짜리 리스트 만들기

for i in number: # number 리스트 (6개 짜리) i로 돌리면서
    for j in range(10): # count_number의 인덱스가 0~9까지니깐 10 넣고
        if i == j: # 만약 i가 j랑 같으면
            count_number[j] += 1 # 요 j를 인덱스로 이용해서 count_number 만들기

# print(count_number) 

# 같은 수 3개가 있는지 찾는 공식
count = 0
for x in count_number: 
    if x >= 3: # 만약 count_number 리스트에 3이상인 x가 있다면
        for z in range(len(count_number)): # 그 X놈의 인덱스를 찾기위해
            if x == count_number[z]: # 찾아버리면
                count_number[z] -= 3  # -3!!!을 해주는 이유 : 연속 3개인 수와 겹칠 수 있음                                           # ex) 5 5 5 4 6 7
    else:
        count += 1 # X가 3이상이지 않으면 count에 1 추가 why ? X가 3이상인 경우가 없으면!
if count == 10: # count는 count_number의 길이만큼 쌓일거고!
    print("babygin 아니요!!!!!")  # 그러면 babygin이 아니뉘깐

else:
    # 연속 3개인 수가 있는지 찾는 공식  ex) count_number = [0, 0, 1, 1, 1, 0, 3, 0, 0, 0]
    for y in range(len(count_number) - 2):  # y가 0부터 7까지 돌아다녀야 함 why? 밑에 y+2가 있으니깐
        # count_number[y]가 1보다는 커야함 why? 그러지 않으면 [0,0, 1, 1, 0, 0, 0, 0, 0, 1] 일 때 0도 아래 공식에 부합함
        if count_number[y] >= 1 and count_number[y] == count_number[y + 1] and count_number[y] == count_number[y + 2]:
 # count_number안에 어떠한 숫자가 1보다 크면서 뒷놈이랑도 같고 뒷뒷놈이랑도 같으면!
            print("babygin 맞음! 야호") # 야호 babygin이네
            break  # 여기까지!
    else: # 그렇지않으면
        print("babygin 아님!") # 끝까지 추적했으나 babygin아님
```

#### 원본풀이🤞

```python
number = list(map(int, input().split()))

count_number = [0]*10

for i in number:
    for j in range(10):
        if i == j:
            count_number[j] += 1



count = 0
for x in count_number:
    if x >= 3:
        for z in range(len(count_number)):
            if x == count_number[z]:
                count_number[z] -= 3 
    else:
        count += 1
if count == 10:
    print("babygin 아니요!!!!!")

else:
    for y in range(len(count_number) - 2):  
        if count_number[y] >= 1 and count_number[y] == count_number[y + 1] and count_number[y] == count_number[y + 2]:
            print("babygin 맞음! 야호")
            break
    else:
        print("babygin 아님!")
```



***



### 양쪽 조망권 문제

#### Think Process⚡

1. 인덱스로 양쪽에 두개랑 비교하고
2. 양쪽 총 4개중에 젤 큰 놈이랑 비교하고 뺀게 조망권
3. 근데 내가 더 작아서 마이너스가 되면 pass

#### 코딩풀이👀

```python
# X = [0, 0, 3, 5, 2, 4, 9, 0, 6, 4, 0, 6, 0, 0]

test_case = int(input())

for i in range(1, test_case+1):
    Y = int(input())
    X = list(map(int, input().split()))


    X[0] = X[1] = X[-1] = X[-2] = 0 # 우선 양쪽 끝 2개씩은 다 0층이랬으니 설정하고

    total = 0 # 조망권을 가진 층수를 모두 더해야 하니 가장 바깥에 total 설정
    for i in range(len(X)-4): # i를 0부터 잡고 i+4까지 해야하니 len(X)에 -4해줌
                              # 시작을 2부터 하면서 i의 양쪽을 표현하는게 더 깔끔할듯
        a = X[i+2] - X[i] # i+2 기준에서 왼쪽 옆의 옆 건물이랑 뺀 값
        b = X[i+2] - X[i+1] # i+2 기준에서 왼쪽 바로 옆 건물이랑 뺀 값
        c = X[i+2] - X[i+3] # i+2 기준에서 오른쪽 옆의 옆 건물이랑 뺀 값
        d = X[i+2] - X[i+4] # i+2 기준에서 오른쪽 바로 옆 건물이랑 뺀 값

        A = [a, b, c, d]  # i+2 기준에서 양쪽 4개 건물이랑 뺀 값을 모은 리스트

        for a in A: 
            min = 9999  # 저 리스트에서 최소값을 구해야함
            for b in range(len(A)):
                if A[b] < min: # 만약 A의 b인덱스가 min보다 작으면
                    min = A[b] # min = A의 b인덱스 즉 이런식으로 A리스트의 가장 작은 수 구하기
        if min > 0 : # 근데 그 최솟값이 음수면 의미가 없으므로 양수일 경우만!
            total += min  # total에 더해줌

    print("#{} {}".format(test_case, total))
    
# 런타임 에러 떴음...기준이 30초인데 1분 38초 ㅎ
```

#### 원본코드⚡

```python
test_case = int(input())

for i in range(1, test_case+1):
    Y = int(input())
    X = list(map(int, input().split()))


    X[0] = X[1] = X[-1] = X[-2] = 0

    total = 0
    for i in range(len(X)-4):

        a = X[i+2] - X[i]
        b = X[i+2] - X[i+1]
        c = X[i+2] - X[i+3]
        d = X[i+2] - X[i+4]

        A = [a, b, c, d]

        for a in A:
            min = 9999
            for b in range(len(A)):
                if A[b] < min:
                    min = A[b]
        if min > 0 :
            total += min

    print("#{} {}".format(test_case, total))
```

