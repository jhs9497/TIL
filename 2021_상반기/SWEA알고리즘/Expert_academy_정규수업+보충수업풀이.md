### <gravity 문제>

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



### <babygin 찾기 문제>

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



### <양쪽 조망권 문제>

#### Think Process⚡

1. 인덱스로 양쪽에 두개랑 비교하고
2. 양쪽 총 4개중에 젤 큰 놈이랑 비교하고 뺀게 조망권
3. 근데 내가 더 작아서 마이너스가 되면 pass

#### 코딩풀이👀

```python
# X = [0, 0, 3, 5, 2, 4, 9, 0, 6, 4, 0, 6, 0, 0]

for tc in range(1, 11): # 테스트 갯수는 무조건 10개니깐 이렇게 합시다이
    Y = int(input())
    X = list(map(int, input().split()))  # X는 빌딩의 층수들


    # X[0] = X[1] = X[-1] = X[-2] = 0 # 우선 양쪽 끝 2개씩은 다 0층이랬으니 설정하고

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

    print("#{} {}".format(tc, total))
    
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

#### 원종님이랑 푼거



```python
for tc in range(1, 11):
    Y = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    for i in range(len(lst)-2):
    #cnt = 0
        if lst[i + 2] > lst[i] and lst[i + 2] > lst[i + 1] and lst[i + 2] > lst[i + 3] and lst[i + 2] > lst[i + 4]:
            A = [lst[i], lst[i+1], lst[i+3], lst[i+4]]

            for z in range(len(A)-1):

                if A[0] < A[z+1]:
                    A[0] = A[z+1]

            cnt += lst[i+2] - A[0]
    print("#{} {}".format(tc, cnt))
   
```



---



### <문자 사각형 1>

정사각형의 한 변의 길이 n을 입력받은 후 다음과 같은 문자로 된 정사각형 형태로 출력하는 프로그램을 작성하시오.

문자의 진행 순서는 맨 오른쪽 아래에서 위쪽으로 'A'부터 차례대로 채워나가는 방법으로 아래 표와 같이 왼쪽 위까지 채워 넣는다.
'Z' 다음에는 다시 'A'부터 반복된다.

< 처리조건 >
첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 10 )
각 케이스의 첫 줄에 N이 주어진다. ( 1 ≤ n ≤ 10 )

<힌트>
ASCII 코드를 문자로 바꾸는 함수는 chr()이고
문자를 ASCII코드로 바꾸는 함수는 ord()이다.
(예) ord('A') , chr(65)


입력

```
3
1
3
5
```

출력

```
#1
A
#2
I F C
H E B
G D A
#3
Y T O J E
X S N I D
W R M H C
V Q L G B
U P K F A
```



#### Think Proccss ⚡

1.  아스키코드를 이용하자
2.  2차원배열을 거꾸로 활용하자
3.  결국 답은 str로 뽑아야한다
4.  줄을 바꿔가며 출력을 해야하니 반복문 안에서 출력이 되게끔 하자

#### 코딩풀이 👀

```python
# A = chr(65)
# print(A)

# 'A'~'Z'를 뽑기 위한 아스키코드 숫자는 65~90

for tc in range(1, int(input())+1):
    # 우선 빈 문자열로 이루어진 N X N 배열을 만들자
    N = int(input())
    answer = [['']*N for _ in range(N)]
    # 행렬의 오른쪽 맨아래부터 위로, 오른쪽부터 왼쪽으로 움직이며 빈 스트링을 채운다.
    # N = 3 이라면 행 렬 모두 2,1,0 순으로 출력되며 인덱싱 해야한다
    asci = 65  # 시작점인 A를 지칭하는 asci 숫자 세팅
    for i in range(N-1, -1, -1): # 2, 1, 0
        for j in range(N-1, -1, -1): # 2, 1, 0
            # 열을 고정시켜야 하므로 i를 뒤로로
            answer[j][i] = chr(asci)  # -> 문자열 'A'를 뜻함
            asci += 1 # ABCDEF로 움직여야 하니깐 1 추가
            if asci == 91:  # 위에 1더하는 것 까지 합쳐서 만약 asci가 90
                asci = 65   # 즉 Z를 뽑는 숫자까지 온다면 65로 초기화하며 다시 A부터 뽑히도록 
    print('#{}'.format(tc))  # 넘버 먼저 뽑고

    # 리스트로 된 answer를 스트링화 하자
    for a in range(len(answer)):
        real_answer = '' # 한줄 씩 뽑고 바로 초기화
        for b in range(len(answer)):
            real_answer += answer[a][b]
            real_answer += ' ' # 띄어쓰기 해주기
        print(real_answer) # 한 줄씩 answer 행렬 뽑아주기
```



---



### <문자 사각형 2>

#### Think Proccss ⚡

1.  문자사각형과 비슷한 문제
2. 한번의 for문으로 하기 힘들어 보인다
3. 홀수/짝수 경우를 나눠서 생각하자
4. 세로줄 한 줄 씩 끊어서 넣자
5. 아스키코드가 끊기지 않으면서 세로줄은 한 줄 씩 끊어줘야함

#### 코딩풀이 👀

```python
# A = chr(65)
# print(A)

# 'A'~'Z'를 뽑기 위한 아스키코드 숫자는 65~90

for tc in range(1, int(input())+1):
    # 우선 빈 문자열로 이루어진 N X N 배열을 만들자
    N = int(input())
    answer = [['']*N for _ in range(N)]
    # 열 기준 0,1,3,5, 는 아래로 향하게 2,4,6,8 은 위로 향하게 (문자사각형2처럼)
    asci = 65  # 시작점인 A를 지칭하는 asci 숫자 세팅
    count = 1 # 몇번째 시돈지 count하기 위한 용도
    M = 0 # 고정된 열을 표현
    for _ in range(N): # 세로줄로 한번씩 채워나갈 것이기 때문에 N X N 행렬에서 N번 반복해야한다
        if count % 2 == 0: # 만약 count가 홀수면 왼쪽에서 두번째 세로줄이라는 뜻이므로 아래에서 위로 인덱싱
            for j in range(N-1, -1, -1): # 문자사각형1 문제처럼 푼다
                answer[j][M] = chr(asci)  # 여기서 열은 M으로 고정되야 해서 위에 M값을 줌
                asci += 1
                if asci == 91: 
                    asci = 65   
            count += 1  # 세로 1줄이 끝나면 count와 M을 모두 1씩 증가시켜서 다음 세로줄을 표현해준다
            M += 1 
        else: # count가 홀수면
            for j in range(N): # 동일하지만 위에서 아래로 인덱싱 해야하므로 j가 0 1 2 3 4 5이렇게 나오게 해준다
                answer[j][M] = chr(asci)    
                asci += 1 
                if asci == 91: 
                    asci = 65   
            count += 1
            M += 1

    print('#{}'.format(tc)) 
    # 리스트로 된 answer를 스트링화 하자
    for a in range(len(answer)):
        real_answer = '' # 한줄 씩 뽑고 바로 초기화
        for b in range(len(answer)):
            real_answer += answer[a][b]
            real_answer += ' ' # 띄어쓰기 해주기
        print(real_answer) # 한 줄씩 answer 행렬 뽑아주기

```



---



### <GNS.>



숫자 체계가 우리와 다른 어느 행성이 있다. 아래는 이 행성에서 사용하는 0 ~ 9의 값을 순서대로 나타낸 것이다.

**"ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"**

0 ~ 9 의 값을 나타내는 단어가 섞여 있는 문자열을 받아 작은 수부터 차례로 정렬하여 출력하는 프로그램을 작성하라.

예를 들어 입력 문자열이 **"TWO NIN TWO TWO FIV FOR"** 일 경우 정렬한 문자열은 **"TWO TWO TWO FOR FIV NIN"** 이 된다.

**[입력]**

입력 파일의 첫 번째 줄에는 테스트 케이스의 개수가 주어진다.

그 다음 줄에 #기호와 함께 테스트 케이스의 번호가 주어지고 공백문자 후 테스트 케이스의 길이가 주어진다.

그 다음 줄부터 바로 테스트 케이스가 주어진다. 단어와 단어 사이는 하나의 공백으로 구분하며, 문자열의 길이 N은 100≤N≤10000이다.

**[출력]**

\#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 정렬된 문자열을 출력한다.

입력10
\#1 7041
SVN FOR ZRO NIN FOR EGT EGT TWO FOR FIV FIV ONE SVN ONE ONE FIV TWO SVN SIX ONE FOR TWO THR TWO TWO ONE SIX EGT FIV SVN SIX ONE EGT NIN TWO SVN NIN FIV FOR THR ONE TWO THR THR FOR ONE ONE THR EGT SVN FOR TWO SVN SVN NIN THR ONE NIN EGT SIX FIV ZRO TWO EGT SIX ZRO TWO FOR EGT SIX FIV ZRO NIN ZRO ZRO SIX ONE THR EGT NIN THR FOR FOR SIX ZRO SIX SIX ONE...
\#2 7778
EGT ONE THR SIX ZRO ZRO NIN FIV FOR EGT SVN FOR NIN NIN EGT THR EGT FIV TWO ONE FIV THR ONE SIX SVN THR ZRO FIV TWO TWO ONE FIV ZRO TWO SIX TWO EGT THR SIX SVN FOR FIV THR SVN SVN EGT EGT FOR ZRO THR FIV EGT NIN THR ONE SVN ZRO NIN THR THR FIV SVN THR SIX FOR NIN FOR ZRO ZRO NIN SVN EGT SIX FIV TWO TWO THR FIV THR SVN NIN ONE ZRO FIV ZRO NIN THR SIX ...
...]

출력#1
ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ...
\#2
ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ...

#### Think Proccss ⚡

1.  인덱스를 이용해서 문자열을 우리가 아는 숫자열로 바꿔주자
2.  그 숫자열을 버블정렬해주자
3.  다시 문자열로 변환

#### 코딩풀이 👀

```python
for tc in range(1, int(input())+1):
    num, N = input().split()
    N = int(N)
    
    print('#{}'.format(tc))

    int_list = ['ZRO','ONE','TWO',"THR","FOR","FIV",'SIX',"SVN",'EGT','NIN']

    # 문자열을 리스트로 받자
    ailen_number = list(map(str, input().split()))

    # 이 문자열을 숫자열로 바꿔주자
    earth_number = []
    for i in ailen_number:
        for j in range(len(int_list)):
            if i == int_list[j]:
                earth_number += [j]

    # 바뀐 숫자열 버블정렬
    for a in range(N-1):
        for b in range(N-1):
            if earth_number[b] > earth_number[b+1]:
                earth_number[b], earth_number[b+1] = earth_number[b+1], earth_number[b]
    
    # 맨 처음 했던것의 반대로 이번엔 숫자열을 문자열로
    answer = ''
    for a in earth_number:
        for b in range(len(int_list)):
            if a == b:
                answer += int_list[b]
                answer += ' ' # 공백추가

    print(answer)
```



#### 배워야할 접근법👍

```python
T = int(input())
 
for tc in range(1, T+1):
 
    tc_num, N = map(str, input().split())
    N = int(N)
     
    print("#{}".format(tc))
 
    # print(tc_num, N, type(N))
 
    str_nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    str_dict = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
    num_cnt = [0]*len(str_nums)
 
    input_data = list(map(str, input().split()))
 
    for i in range(N):
        if input_data[i] in str_dict: # ONE
            num_cnt[str_dict[input_data[i]]] += 1 
 
    for i in range(len(num_cnt)):
        print((str_nums[i]+' ') * num_cnt[i])  # 이런게 가능했었군!
        
# 혜은님 코드인데 너무 간단하게 잘 코딩하셔서 놀랐음
# dict와 list를 정말 조화롭게 잘 활용한 것 같다
```



### <문자열 비교>

두 개의 문자열 str1과 str2가 주어진다. 문자열 str2 안에 str1과 일치하는 부분이 있는지 찾는 프로그램을 만드시오.

예를 들어 두 개의 문자열이 다음과 같이 주어질 때, 첫 문자열이 두번째에 존재하면 1, 존재하지 않으면 0을 출력한다.


ABC

ZZZZZ**ABC**ZZZZZ

두번째 문자열에 첫번째 문자열과 일치하는 부분이 있으므로 1을 출력.


ABC

ZZZZ**A**Z**BC**ZZZZZ

문자열이 일치하지 않으므로 0을 출력.

**[입력]**


첫 줄에 테스트 케이스 개수 T가 주어진다. (1≤T≤50)


다음 줄부터 테스트 케이스 별로 길이가 N인 문자열 str1과 길이가 M인 str2가 각각 다른 줄에 주어집니다. (5≤N≤100, 10≤M≤1000, N≤M)

 

**[출력]**


각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

입력

3 XYPV EOGGXYPVSY STJJ HOFSTJPVPP ZYJZXZTIBSDG TTXGZYJZXZTIBSDGWQLW

출력

#1 1 #2 0 #3 1



#### Think Proccss ⚡

1.  기준이되는 문자열과 움직이는 문자열이 있다
2.  움직이는 문자열의 인덱스는 고정
3.  기준이되는 문자열의 인덱스는 움직이는 문자열의 인덱스에 따라 변화하게 만든다
4.  기준이 되는 문자열 인덱스의 기준은 움직이는 문자열의 길이랑 같다.

#### 코딩풀이 👀

```python
for tc in range(1, int(input())+1):
    str1 = input()
    N = len(str1) # 움직이는 스트링
    str2 = input()
    M = len(str2)  # 기준 스트링

    # N = 4
    # M = 10 이라 가정

    answer = 0
    for i in range(M-N+1): # i = 0,1,2,3,4,5,6,7 (str2의 인덱싱)
        str1_1 = ''
        str2_2 = ''
        for j in range(N): # j = 0,1,2,3 (str1의 인덱싱)
            str1_1 += str1[j]
            str2_2 += str2[i+j]

        if str1_1 == str2_2:
            answer += 1

    if answer > 0:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))

```



---



### <회문>

ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다. NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.

회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.


예를 들어 N=10, M=10 일 때, 다음과 같이 회문을 찾을 수 있다.


| G    | O    | F    | F    | A    | K    | W    | F    | S    | M    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| O    | Y    | E    | C    | R    | S    | L    | D    | L    | Q    |
| U    | J    | A    | J    | Q    | V    | S    | Y    | Y    | C    |
| J    | A    | E    | Z    | N    | N    | Z    | E    | A    | J    |
| W    | J    | A    | K    | C    | G    | S    | G    | C    | F    |
| Q    | K    | U    | D    | G    | A    | T    | D    | Q    | L    |
| O    | K    | G    | P    | F    | P    | Y    | R    | K    | Q    |
| T    | D    | C    | X    | B    | M    | Q    | T    | I    | O    |
| U    | N    | A    | D    | R    | P    | N    | E    | T    | Z    |
| Z    | A    | T    | W    | D    | E    | K    | D    | Q    | F    |

 

**[입력]**


첫 줄에 테스트 케이스 개수 T가 주어진다. 1≤T≤50

다음 줄부터 테스트케이스의 첫 줄에 N과 M이 주어진다. 10≤N≤100, 5≤M≤N

다음 줄부터 N개의 글자를 가진 N개의 줄이 주어진다.



#### Think Proccss ⚡

1.  입력에 공백이 없으므로 우선 입력값을 내가 원하는 자료형으로 변환해야한다
2.  각각 스트링으로 이루어진 리스트로 변환
3.  모든 M크기의 행과 열을 뽑자
4.  그 행렬이 회문인지 확인하자
5.  회문이면 그 행렬을 뽑자



#### 코딩풀이 👀

```python
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
#     # N X N 글자판에서
#     # M길이의 회문을 찾아라
#
#     # 전체 보드를 만들고
    first_board = [list(input().split()) for _ in range(N)]
    # ['G','O','F','F'] 이런식으로 만들고 싶은데..
    str_board = [['']*N for _ in range(N)]
    # 리스트를 스트링화해서 하나씩 새로운 str_board에 넣기
    for a in range(N):
        A = ''.join(first_board[a])
        for b in range(len(A)):
            str_board[a][b] = A[b]

    # 행과 열 검색
    answer = []
    for a in range(N): # 이 for문을 통해 위 아래도 표현
     
        for i in range(N-M+1): # 문자열 검색과 같음 선 위에서 움직임 (i는 인덱스로 활용 X j를 표현하기 위함임)
            # 행 후보군
            answer_R = []
            # 열 후보군
            answer_C = []
            for j in range(i, i+M): 
                answer_R += str_board[a][j]  # 주의할점 a가 행을 의미하고 j가 열을 의미함 i는 사용 X
                answer_C += str_board[j][a]

            L = len(answer_R) # 뽑아진 행or렬의 길이를 구하고

            # 슬라이싱을 이용해 비교
            # 맨앞에서 절반까지의 슬라이싱과 맨뒤에서 절반까지 거꾸로 슬라이싱해서 비교
            if L % 2 == 1: # N이 홀수라면
                if answer_R[0:L//2] == answer_R[L:L//2:-1]:
                    answer = answer_R
                if answer_C[0:L//2] == answer_C[L:L//2:-1]:
                    answer = answer_C
            else: # N이 짝수라면
                if answer_R[0:L//2] == answer_R[L:L//2-1:-1]:
                    answer = answer_R
                if answer_C[0:L // 2] == answer_C[L:L // 2 - 1:-1]:
                    answer = answer_C

    # 현재 내가 갖고 있는 정답은 리스트이므로 스트링화
    answer = ''.join(answer)

    print('#{} {}'.format(tc, answer))

```



### <달팽이>



#### 코딩풀이 👀

```python
for tc in range(1, int(input())+1):
    N = int(input())

    # 우선 0으로 이루어진 2차원 배열을 만들자

    snail = [[0]*N for _ in range(N)]

    # 어렵게 생각하지 말자

    x = 0
    y = -1
    trans = 1
    cnt = 1

    while N > 0:
        for _ in range(N):
            y += trans
            snail[x][y] = cnt
            cnt += 1

        N -= 1
        for _ in range(N):
            x += trans
            snail[x][y] = cnt
            cnt += 1
            
        trans *= -1


    print('#{}'.format(tc))
    
    
    
    for i in range(len(snail)):
        snail_answer = ''
        for j in range(len(snail)):
            snail_answer += str(snail[i][j])
            snail_answer += ' '
        print(snail_answer)
```

#### 원종님 풀이 공유

```python
n = 3

snail = [[0] * n for _ in range(n)]
#초기 좌표 및 값
x, y = 0, 0
snail[x][y] = 1
# 방향
dx = [0,1,0,-1]
dy = [1,0,-1,0]
mode = 0
for num in range(2, n*2+1):
    x += dx[mode]
    y += dy[mode]
    snail[x][y] = num
    if 0 <= x + dx[mode] < n and 0 <= y + dy[mode] < n and not snail[x+dx[mode]][y+dy[mode]]:
        continue

    if mode != 3:
        mode += 1
    else:
        mode = 0
for i in snail:
    print(*i)
```



### <문자열 비교>



#### 코딩풀이 👀

```python
for tc in range(1, int(input())+1):
    str1 = input()
    N = len(str1) # 움직이는 스트링
    str2 = input()
    M = len(str2)  # 기준 스트링

    # N = 4
    # M = 10 이라 가정

    answer = 0
    for i in range(M-N+1): # i = 0,1,2,3,4,5,6,7 (str2의 인덱싱)
        str1_1 = ''
        str2_2 = ''
        for j in range(N): # j = 0,1,2,3 (str1의 인덱싱)
            str1_1 += str1[j]
            str2_2 += str2[i+j]

        if str1_1 == str2_2:
            answer += 1

    if answer > 0:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))

```



### <빠른 타이핑>



#### 코딩풀이 👀

```python
for tc in range(1, int(input())+1):
    A, B = input().split()  #6  #4

    if len(B) == 1:  # B의 길이가 1이면 바로 A의 길이만큼 프린트
        print('#{} {}'.format(tc, len(A)))
        break
    else:
        count = 0 # A랑 B가 같으면 +1 씩
        idx = 0 # A의 탐색 시작 인덱스 (계속 움직여야)
        a = len(A) # A의 길이이자 남은 A열의 길이로 사용하자
        b = len(B)
        while a >= b: # A의 길이가 B보다 커져버리면 의미가 없으므로
            A_ = '' # A 패턴 후보군
            for i in range(idx, idx+b): # idx값이 변화하면서 A의 인덱싱을 조절함
                A_ += A[i]
            B_ = '' # 고정된 B 패턴
            for j in range(b): # B는 항상 고정
                B_ += B[j]

            if A_ == B_: # 만약 A랑 B의 패턴이 같다면
                count += 1 # count +1 해주고
                idx += b # 시작 인덱스를 b만큼 뛰어넘어줘야함 why? 만약 A = AOAOAOAOAOAOA B = AOA이면 뛰어넘지 않을시 중첩
                a -= b # 뛰어 넘은만큼 남은 A의 길이도 b로 빼준다
            else: # 값이 다르다면
                idx += 1  # 다음 칸을 탐색한다
                a -= 1

    answer = len(A)- count*len(B) + count

    print('#{} {}'.format(tc, answer))
```
