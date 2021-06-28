### 1945. 간단한 소인수분해

> 숫자 N은 아래와 같다.
>
> N=2a x 3b x 5c x 7d x 11e
>
> N이 주어질 때 a, b, c, d, e 를 출력하라.
>
> 
> **[제약 사항]**
>
> N은 2 이상 10,000,000 이하이다.
>
> 
> **[입력]**
>
> 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
>
> 각 테스트 케이스의 첫 번째 줄에 N 이 주어진다.
>
> **[출력]**
> 
>출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
> 
>(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
> 
>입력
> 
>10 
> 6791400
> 1646400
> 1425600
> 8575
> 185625
> 6480
> 1185408
> 6561
> 25
> 330750
> 
>출력
> 
>#1 3 2 2 3 1
> \#2 6 1 2 3 0
> \#3 6 4 2 0 1
> \#4 0 0 2 3 0
> \#5 0 3 4 0 1
> \#6 4 4 1 0 0
> \#7 7 3 0 3 0
> \#8 0 8 0 0 0
> \#9 0 0 2 0 0
> \#10 1 3 3 2 0



#### Think Process ⚡

1. N을 a, b, c, d, e로 각각 나누어서 나누어 떨어지면 그 횟수를 count해야한다.
2. if문을 이용한다면 횟수를 count하긴 어렵다.
3. while문을 이용하자
4. 파이썬은 위에서 아래로 순서대로 이루어지므로 if elif else구문을 사용할 필요 없을 듯 하다
5. 어차피 2, 3, 5, 7, 11만 물어보고 있으니 47과 같은 서로소는 고려 X

#### 코딩 풀이 👀

```python
test_case = int(input())
for i in range(test_case):
    N = int(input())
    
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0

    while N % 2 ==0:
        N = N / 2
        a += 1
    
    while N % 3 ==0:
        N = N / 3
        b += 1  

    while N % 5 ==0:
        N = N / 5
        c += 1

    while N % 7 ==0:
        N = N / 7
        d += 1


    while N % 11 ==0:
        N = N / 11
        e += 1
    
    print(f'#{i+1} {a} {b} {c} {d} {e}')
```



***



### 1926. 간단한 369게임

> 3 6 9 게임을 프로그램으로 제작중이다. 게임 규칙은 다음과 같다.
>
>  
>
> \1. 숫자 1부터 순서대로 차례대로 말하되, **“3” “6” “9”** 가 들어가 있는 수는 말하지 않는다.
>
>  **1 2** **3** **4 5** **6** **7 8** **9…**
>
> \2. "3" "6" "9"가 들어가 있는 수를 말하지 않는대신, 박수를 친다. 이 때, 박수는 해당 숫자가 들어간 개수만큼 쳐야 한다. 
> 예를 들어 숫자 35의 경우 박수 한 번, 숫자 36의 경우 박수를 두번 쳐야 한다.
>
> 입력으로 정수 N 이 주어졌을 때, 1~N 까지의 숫자를
>
> 게임 규칙에 맞게 출력하는 프로그램을 작성하라.
>
> 박수를 치는 부분은 숫자 대신, 박수 횟수에 맞게 “-“ 를 출력한다.
>
> **여기서 주의해야 할 것은 박수 한 번 칠 때는 - 이며, 박수를 두 번 칠 때는 - - 가 아닌 -- 이다. 
> ** 
>
> **[제약사항]**
>
> N은 10이상 1,000이하의 정수이다. (10 ≤ N ≤ 1,000)
>
>  
>
> **[입력]**
>
> 입력으로 정수 N 이 주어진다.
>
> 
> **[****출력]**
>
> 1 ~ N까지의 숫자를 게임 규칙에 맞게 출력한다.
>
> 
>
> 입력10
>
> 출력1 2 - 4 5 - 7 8 - 10



#### Think Process ⚡

1. 컴퓨터가 369를 하려면 어떤 방식이 필요할까
2. 숫자를 자리마다 하나씩 쪼개서 보개 만들면 가능할까
3. 쪼개서 그 쪼갠 자릿수가 3,6,9안에 있다면 결과str에 추가하는 방식으로 해보자
4. 문제가 생겼다 ex) 359같은 경우 -5- 이런식으로 추가된다.
5. 다른 방법을 찾아야 한다 자릿수가 3,6,9에 속한 횟수만큼 하이푼을 추가할 수 없을까
6. 이중포문을 이용해보자
7. 첫 번째 for문에선 인덱싱 할 숫자가 나오게하고
8. 두 번째 for문에선 그 숫자의 길이만큼 for문을 돌리며 시도해보자
9. GREAT! GO!

#### 코딩 풀이 👀

```python
N = int(input())

# 3, 6, 9를 담은 str A를 만들고
A ='3', '6', '9'

# 답도 빈 스트링으로 표현
Answer = ''

# 1~input(N)까지를 for문으로 돌리면서
for i in range(1, N+1):
    # i값을 문자화하여 B로 저장 why? 인덱싱을 위해
    B = str(i)
    # 문자화된 해당 i가 3,6,9에 일치한 횟수를 count하기 위한 변수 count
    count = 0
    # 이중 for문으로 B의 길이만큼 돌린다.why? 인덱싱할 길이니깐
    for j in range(len(B)):
        # 만약 B의 인덱싱값이 A (3,6,9) 안에 있다면
        if B[j] in A:
            # count에 1을 더해준다.
            count += 1
     # 만약 count가 한 번도 일어나지 않아 count가 0이라면
    if count == 0:
        # Answer에는 B를 그대로 더해주고
        Answer += B
    else:
        # count가 한 번이라도 일어났다면 '-'를 count수만큼 곱해서 더해준다.
        Answer += '-'*count
      # 사이사이 빈 칸이 필요하므로 Answer에 빈 칸은 밑에 for문이 끝날 때 마다 한 번씩 더해준다.
    Answer += ' '
        
print(Answer)
```

#### 원본 코딩 🤞

```python
N = int(input())

A ='3', '6', '9'

Answer = ''

for i in range(1, N+1):
    B = str(i)
    count = 0
    for j in range(len(B)):
        if B[j] in A:
            count += 1
    if count == 0:
        Answer += B
    else:
        Answer += '-'*count
    Answer += ' '
        
print(Answer)
```



***



### 2007. 패턴 마디의 길이

> 각 문자열의 길이는 30이다. 마디의 최대 길이는 10이다.
>
> 
> **[입력]**
>
> 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
>
> 각 테스트 케이스의 첫 번째 줄에는 길이가 30인 문자열이 주어진다.
>
> 
> **[출력]**
>
> 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
>
> (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
>  
>
> 입력
>
> 3    
> KOREAKOREAKOREAKOREAKOREAKOREA
> SAMSUNGSAMSUNGSAMSUNGSAMSUNGSA
> GALAXYGALAXYGALAXYGALAXYGALAXY   
>
> 출력
>
> #1 5
> \#2 7



#### Think Process ⚡

1. 단어가 같다는 것을 컴퓨터가 어떻게 알 수 있을까
2. 예제를 보니 반복단어는 우선 첫글자부터 시작되는 것 같다.
3. 슬라이싱을 활용하면 될 거 같은데
4. 반복문과 슬라이싱, 0부터의 인덱스를 이용해서 코딩해보자 

#### 코딩 풀이 👀

```python
# test_case 개수 인풋으로 받고
test_case = int(input())
# 인풋 값만큼 for문 돌리며
for i in range(test_case):
    # input값들을 빈칸 기준으로 나누며 str화하여 list에 담아 변수에 저장
    senten = list(map(str,input().split()))
   # senten for문 돌리며
    for sen in senten:
        # 문자열의 최대 길이가 10이랬으므로 1~10 for문 돌린다
        for j in range(1,11):
# 만약 0~j까지의 인덱싱과 j+1~ 2*(j+1)의 값이 같다면 같은 단어가 연달아 있는 인덱싱범위를 구한 셈
            if senten[0][0:j+1] == senten[0][j+1: 2*(j+1)]:
               # 0부터 인덱싱한 j+1을 출력하면 그 글자의 길이를 구할 수 있다.
                print(f'#{i+1} {j+1}')
               # 답나왔으니 이후 for문은 돌릴 필요 없으므로 break
                break
```

#### 원본 코딩 🤞

```python
test_case = int(input())
for i in range(test_case):
    senten = list(map(str,input().split()))

    for sen in senten:
        for j in range(1,11):


            if senten[0][0:j+1] == senten[0][j+1: 2*(j+1)]:
                print(f'#{i+1} {j+1}')
                break
```



***



#### 2001. 파리 퇴치

>N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미한다.
>
>아래는 N=5 의 예이다.
> 
>
>![img](fileDownload.do)
>
>
>M x M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다.
>
>죽은 파리의 개수를 구하라!
>
>예를 들어 M=2 일 경우 위 예제의 정답은 49마리가 된다.
>
>![img](fileDownload.do)
>
>
>
>**[제약 사항]**
>
>\1. N 은 5 이상 15 이하이다.
>
>\2. M은 2 이상 N 이하이다.
>
>\3. 각 영역의 파리 갯수는 30 이하 이다.
>
>
>**[입력]**
>
>가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
>
>각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,
>
>다음 N 줄에 걸쳐 N x N 배열이 주어진다.
>
>
>**[출력]**
>
>출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
>
>(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
>
>
>
>입력10
>5 2
>1 3 3 6 7
>8 13 9 12 8
>4 16 11 12 6
>2 4 1 23 2
>9 13 4 7 3
>6 3
>29 21 26 9 5 8
>21 19 8 0 21 19
>9 24 2 11 4 24
>19 29 1 0 21 19
>10 29 6 18 4 3
>29 11 15 3 3 29
>...
>
>출력#1 49
>\#2 159
>...



#### Think Process ⚡

1. N과 M을 가지고 모든 경우를 표현할 수 있도록 만들어야한다.
2. N X N 전체 판을 리스트로 쭉 늘려서 생각하자.
3. 기준점이 되는 인덱스를 정하고 옮기면서 사각형을 만들어보자.
4. 기준점이 되는 인덱스는 범위가 좁아진다. 그 범위 또한 N, M을 이용해서 만들어야함

#### 코딩 풀이 👀

```python
test_case = int(input())
 
for b in range(test_case):
     
 
    N, M = map(int ,input().split())
 
 
    N_list = []  # i의 범위에서 제외가 되는 list
 
    for x in range(1, 100):
        for y in range(1, M):
            X = N*x - y  # 각 N의 배수에서 0, 1, ..., M까지 밴 범위
            N_list.append(X)
 
    Key_number = (N**2) - (M-1) - N*(M-1)  # 기준이 되는 i의 활동 범위 
    
    # 우선 i는 파리채의 왼쪽 맨위로 삼았음
    # 만약 N = 5 , M = 2라서 5X5 전체 판에 2 X 2 파리채라면
    # 밑에 사진으로 설명
 
    original_list = [] # N X N 판을 일렬 list로 표현
 
    for a in range(N):
     
     
        number= list(map(int, input().split()))
        original_list += number
     
 
    potential_list = []  # 후보가 되는 파리채 점수 리스트

    for i in range(Key_number):  # 아까 구한 i의 가능범위까지 돌리면서     

        if i in N_list: # 만약 i가 제외 리스트에 포함되면 continue
            continue    

        else: # 제대로 동작한다면  # 현재 i는 위에 for문에서 설정된 친구
            total = 0 # i에 해당하는 사각형의 합을 담을 그릇
            for j in range(0, M): # i는 고정인 상태에서 파리채 크기(M)만큼 for문 이건 세로
                for z in range(0, M): # i는 고정인 상태에서 파리채 크기(M)만큼 for문 이건 가로
                    total += original_list[i + (j*N) + z]#i는 고정인덱스, j*N는 세로 z는 가로
            potential_list.append(total) # 답이 될 수 있는 potential_list에 추가 
                                         # 즉 파리채가 칠 수 있는 모든 사각형의 합이 각각 추가

    answer = max(potential_list) # 그 후보들 중에서 젤 큰놈으로다가 answer로 설정

    print(f'#{b+1} {answer}')
```



![KakaoTalk_20210209_005132374](KakaoTalk_20210209_005132374.png)

#### 원본 코딩 🤞

```python
test_case = int(input())
 
for b in range(test_case):
     
 
    N, M = map(int ,input().split())
 
 
    N_list = []  # N의 배수 -1 을 담은 리스트
 
    for x in range(1, 100):
        for y in range(1, M):
            X = N*x - y
            N_list.append(X)
 
    Key_number = (N**2) - (M-1) - N*(M-1)  # 기준이 되는 i의 활동 범위
 
    original_list = []
 
    for a in range(N):
     
     
        number= list(map(int, input().split()))
        original_list += number
     
 
    potential_list = []  # 후보가 되는 파리채 점수 리스트

    for i in range(Key_number):  # 0~ 18까지 돌면서 5의배수 -1 에서는 continue를 해줘야함      

        if i in N_list:
            continue    

        else:
            total = 0
            for j in range(0, M):
                for z in range(0, M):
                    total += original_list[i + (j*N) + z]
            potential_list.append(total)

    answer = max(potential_list)

    print(f'#{b+1} {answer}')
```



***



###  1989. 초심자의 회문 검사

>"level" 과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.
>
>단어를 입력 받아 회문이면 1을 출력하고, 아니라면 0을 출력하는 프로그램을 작성하라.
>
>
>**[제약 사항]**
>
>각 단어의 길이는 3 이상 10 이하이다.
>
>
>**[입력]**
>
>가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
>
>각 테스트 케이스의 첫 번째 줄에 하나의 단어가 주어진다.
>
>
>**[출력]**
>
>출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
>
>(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
>
>입력
>
>3
>level   
>samsung
>eye    
>
>출력
>
>#1 1
>\#2 0
>\#3 1



#### Think Process ⚡

1. 다시풀기...

#### 코딩 풀이 👀

```python
test_case = int(input())

for i in range(test_case):
    sample = str(input())
    
    if len(sample) % 2 == 0:
        print(f'#{i+1} 0')
    
    else:
        A_list = []
        
        for a in range(len(sample)//2):
            A_list.append(a)
        
        B_list = []
        for b in range(len(sample)//2, len(sample)):
            B_list.append(b)
            
        B_list.reverse()
        
    if A_list == B_list:
        print(f'#{i+1} 1')
            
```

#### 원본 코딩 🤞

```python

```



***

