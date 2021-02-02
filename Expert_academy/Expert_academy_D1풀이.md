### 2058. 자릿수 더하기

> 하나의 자연수를 입력 받아 각 자릿수의 합을 계산하는 프로그램을 작성하라.
>
>
> **[제약 사항]**
>
> 자연수 N은 1부터 9999까지의 자연수이다. (1 ≤ N ≤ 9999)
>
>
> **[입력]**
>
> 입력으로 자연수 N이 주어진다.
>
>
> **[출력]**
>
> 각 자릿수의 합을 출력한다.
>
> 
>
> 입력 6789   출력 30



```python
test_case = int(input())
# input을 숫자로 받는다 (int가 없어도 상관은 없을 것 같다.)

numbers = str(test_case)
# input값이 담긴 test_case를 str값으로 바꾼다.
# why? int는 반복문을 돌릴 수 없기 때문에

total = 0
# for문에 바깥에 최종 답인 total 변수를 만들고
for i in numbers:
    # str화한 numbers를 for문으로 돌린다.
    total += int(i)
    # total에 더할 때는 총합숫자가 나와야 하므로 다시 int로 형변환하여 더해준다.
print(total)
```



### 2056. 연월일 달력  

> 연월일 순으로 구성된 8자리의 날짜가 입력으로 주어진다.
>  
>
> ![img](https://swexpertacademy.com/main/common/fileDownload.do?downloadType=CKEditorImages&fileId=AV5QOksKA1QDFAUq)
>
> 
> 해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면
>
> [그림1] 과 같이 ”YYYY/MM/DD”형식으로 출력하고,
>
> 날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.
>
> 
> 연월일로 구성된 입력에서 월은 1~12 사이 값을 가져야 하며
>
> 일은 [표1] 과 같이, 1일 ~ 각각의 달에 해당하는 날짜까지의 값을 가질 수 있다.
>
> ![img](https://swexpertacademy.com/main/common/fileDownload.do?downloadType=CKEditorImages&fileId=AV5QOw9qA1UDFAUq)
>
> 
> ※ 2월의 경우, 28일인 경우만 고려한다. (윤년은 고려하지 않는다.)
>
> 
> **[입력]**
>
> 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
>
> 다음 줄부터 각 테스트 케이스가 주어진다.
>
> 
> **[출력]**
>
> 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
>
> (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
>
> 
>
> 입력5
> 22220228
> 20150002
> 01010101
> 20140230
> 11111111
>
> 
>
> 출력
>
> #1 2222/02/28
> \#2 -1
> \#3 0101/01/01
> \#4 -1
> \#5 1111/11/11



```python
test_case = int(input())

for i in range(1, test_case+1):

    number = input()


  # 각 month에 해당하는 str변수를 만들었다 (여기까지는 봐줄만 하다)
    month_A_str = '01', '03', '05', '07', '08', '10', '12'
    month_B_str = '04', '06', '09', '11'
    month_C_str = '02'
    
  # 달마다 일수 차이는 range로 코딩답게 해보려고 했으나 01,02,03,04~09의 한자릿수 일들이 포함이 되지 않았다.
    #date_A_str = str(list(range(1, 32)))
    #date_B_str = str(list(range(1, 31)))
    #date_C_str = str(list(range(1, 29)))   

  # 노가다 시전...
    date_A_str = '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'
    date_B_str = '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30' 
    date_C_str = '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28'



  # input값으로 받은 int를 str화하여 original에 저장
    original = ''
  # for문으로 돌려서 한 글자씩 빼낸다.
    for j in str(number):
        original += j
        
    # case1) 만약 originaldml 숫자 ex) 20201212의 월 부분이 month_A에 속하면서 일 부분이 date_A에 속한다면
    if original[4:6] in month_A_str and original[6:8] in date_A_str:
    # 정답은 아래와 같이 그대로 뽑으면 된다.1111111
        result = original[0:4] + '/' + original[4:6] + '/' + original[6:]
        print(f'#{i}', result)
    # case 2) 그렇지 않고 월 부분이 month_B에 속하면서 일 부분이 date_B에 속한다면
    elif original[4:6] in month_B_str and original[6:8] in date_B_str:
    # 정답은 아래와 같이 그대로 뽑으면 된다.2222222
        result = original[0:4] + '/' + original[4:6] + '/' + original[6:]
        print(f'#{i}', result)
    # case 3) 그렇지 않고 월 부분이 month_C에 속하면서 일 부분이 date_C에 속한다면
    elif original[4:6] in month_C_str and original[6:8] in date_C_str:
    # 정답은 아래와 같이 그대로 뽑으면 된다.3333333
        result = original[0:4] + '/' + original[4:6] + '/' + original[6:]
        print(f'#{i}', result)
   # case 4) 그 어디에도 속하지 못한다면 -1 프린트!!!!
    else:
        print(f'#{i} -1')
        
        
 # 풀긴 풀었으나 찝찝한 느낌...
```



###  2050. 알파벳을 숫자로 변환

> 알파벳으로 이루어진 문자열을 입력 받아 각 알파벳을 1부터 26까지의 숫자로 변환하여 출력하라.
>
> 
> **[제약 사항]**
>
> 문자열의 최대 길이는 200이다.
>
> 
> **[입력]**
>
> 알파벳으로 이루어진 문자열이 주어진다.
>
> 
> **[출력]**
>
> 각 알파벳을 숫자로 변환한 결과값을 빈 칸을 두고 출력한다.
>  
>
> 입력ABCDEFGHIJKLMNOPQRSTUVWXYZ
>
> 
>
> 출력1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26



```python
# 처음에는 그냥 알파벳 input만큼 1부터 차례로 뽑으라는 줄 알고 그렇게 풀었으나 땡!!
# ABCDE~~~ 와 12345~~~~를 순서에 맞게 매칭해줘야 하는 것 같다
# input 값이 CDEAB이라면 output이 34512 가 되도록!


# 우선 혹시 소문자가 input들어올 수~~~도 있으니깐 .upper뒤에 달아준다!
test_case = str(input()).upper()

# 알파벳과 숫자를 매칭해놓은 dict를 먼저 만들어야겠다.
# 알파벳을 담은 변수와 빈 dict를 만들고
alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

alph_dict = {}

# 알파벳의 길이만큼 for문을 돌리며
for i in range(len(alph)):
    # 빈 dict에 키값 = alph의 인덱싱값, 밸류값 = 돌아가는 for문의 i +1 을 넣어준다 
    alph_dict[alph[i]] = i+1
# 여기까지 알파벳 & 숫자 dict 완성!

# test_case에 input된 알파벳들을 for문으로 돌리면서
for char in test_case:
    # 최종 result 값 변수를 만들어놓고
    result = ''
    # 처음에 만들어둔 alph_dict에 key값들을 대상으로 for문을 돌리며
    for i in alph_dict:
        # test_case의 알파벳과 key값이 일치하는 순간
        if char == i:
            # 그 key에 해당하는 밸류값을 최종 reuslt에 str형태로 더해준다
            result += str(alph_dict[char])
            

 # 마지막으로 출력하되 옆으로 한칸 씩 띄워서 출력!
    print(result, end=' ')
    

```



### 2047. 신문 헤드라인

> 신문의 헤드라인을 편집하기 위해, 주어지는 문자열의 알파벳 소문자를 모두 대문자로 바꾸는 프로그램을 개발 중이다.
>
> 입력으로 주어진 문장에 모든 소문자 알파벳을 찾아 대문자로 변환한 다음, 그 결과를 출력하는 프로그램을 작성하라.
>
> 
> **[예제 풀이]**
>
> The_headline_is_the_text_indicating_the_nature_of_the_article_below_it.
>
> 위와 같은 문자열이 입력으로 주어졌을 때, 출력은 다음과 같다.
>
> THE_HEADLINE_IS_THE_TEXT_INDICATING_THE_NATURE_OF_THE_ARTICLE_BELOW_IT.



```python
# test_case str형태로 받고
test_case = str(input())

# 변수에 .upper() 써서 넣은다음
A = test_case.upper()

# 출력
print(A)

# 이게 1단계 문제지😃
```



###  2046. 스탬프 찍기

> 주어진 숫자만큼 # 을 출력해보세요.
>
> 주어질 숫자는 100,000 이하다.
>
> 입력3
>
> 출력###



```python
# test_case int형태로 받고
test_case = int(input())

# 변수에 str# 곱하기 int test_case 하고
answer = '#'*test_case

# 출력
print(answer)

# 이게 1단계 문제지2😁
```



### 2043. 서랍의 비밀번호

> 서랍의 비밀번호가 생각이 나지 않는다.
>
> 비밀번호 P는 000부터 999까지 번호 중의 하나이다.
>
> 주어지는 번호 K부터 1씩 증가하며 비밀번호를 확인해 볼 생각이다.
>
> 예를 들어 비밀번호 P가 123 이고 주어지는 번호 K가 100 일 때, 100부터 123까지 24번 확인하여 비밀번호를 맞출 수 있다.
>
> P와 K가 주어지면 K부터 시작하여 몇 번 만에 P를 맞출 수 있는지 알아보자.
>
> 
> **[입력]**
>
> 입력으로 P와 K가 빈 칸을 사이로 주어진다.
>
> 
> **[출력]**
>
> 몇 번 만에 비밀번호를 맞출 수 있는지 출력한다.
>  
>
> 입력123 100
>
> 
>
> 출력24



```python
# 이걸 도출하는게 조금 힘들었음
# 2개의 값을 input 받는데
# split()을 통해 공백을 만들고 -> 이 부분 잘 이해가 안됨
# map을 통해 해당 input값을 int화 한다음에
# 인덱싱을 해야하므로 list로 바꾸기
numbers = list(map(int, input().split()))

# abs를 통해 numbers 안의 첫번째 - 두번째의 값을 절대값으로 만든 다음 +1 하면 정답~
answer = abs(numbers[0]-numbers[1])+1

print(answer)
```



### 2029. 몫과 나머지 출력하기

> 2개의 수 a, b를 입력 받아, a를 b로 나눈 몫과 나머지를 출력하는 프로그램을 작성하라.
>
> **[제약 사항]**
>
> 각 수는 1이상 10000이하의 정수이다.
>
> 
> **[입력]**
>
> 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
>
> 각 테스트 케이스의 첫 번째 줄에는 2개의 수가 주어진다.
>
> 
> **[출력]**
>
> 출력의 각 줄은 '#t'로 시작하고 공백을 한 칸 둔 다음, 몫을 출력하고 공백을 한 칸 둔 다음 나머지를 출력한다.
>
> (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
>
> 입력
>
> 3  
> 9 2 
> 15 6 
> 369 15    
>
> 출력
>
> #1 4 1
> \#2 2 3
> \#3 24 9



```python
# int 값으로 input받고
test_case = int(input())

# 3가지 case를 돌려볼거니깐 for문으로 range돌리면서
for i in range(test_case):
    # 위에 문제와 마찬가지로 가운데에 공백넣고 list화 하여 변수에 저장
    numbers = list(map(int, input().split()))


   # divmod라는 아주 이쁜 함수를 알게되어
    q, r = divmod(numbers[0], numbers[1])
    
   # 손쉽게 해결 {q} {r}에도 {} 해줘야 한다는 거 주의!
    print(f'#{i+1} {q} {r}')
```



### 2027. 대각선 출력하기

> 주어진 텍스트를 그대로 출력하세요.
>
> 출력
>
> #++++
> +#+++
> ++#++
> +++#+
> ++++#



```python
# 내 풀이

# 원하는 텍스트 박스를 우선 1자로 만들어보자
# 일자로 만들었을 시 아래의 n번째에서 #이 나온다.
numbers = [1, 7, 13, 19, 25]
# 빈 result 변수를 만들고
result =''

# 1~25 (텍스트박스가 5X5이므로) 숫자를 for문으로 돌리며
# 위에 numbers에 해당하면 #을, 아니면 +를 빈 result값에 저장한다.
for i in range(1, 26):
        if i == 
            result += '#'
        else:
            result += '+'
# 여기까지 result 변수에는 #+++++#+++++#+++++#+++++#가 저장되어 있다.

# 최종 답을 낼 answer 빈 str변수를 만들고
answer = ''
# count를 세준다. why? 5X5 박스를 만들어야 하니깐
count = 0
# result를 돌리면서
for i in result:
    # 빈 answer에는 i를 추가하고
    answer += i
    # count에도 1씩 추가한다.
    count += 1
    # count가 5가 되는 순간
    if count == 5:
        # answer를 출력하고 (첫 번째 줄이 출력될 것이다.)
        print(answer)
        # count는 0으로 초기화
        count = 0
        # answer도 빈 str으로 초기화
        answer = ''
        # 완성
```

``` python
# 용재님과 합작풀이
# 용재님의 기존 풀이에 머리를 맞대니 조금 더 프로그램스러운 풀이가 가능했다.

# 우선 number에 -1을 넣고 시작한다. 
# why? 0부터 시작하면 밑에서 +=1을 하기때문에 인덱싱이 1부터 된다 
number = -1
# 0~4까지의 숫자 for문을 돌리면서
for re in range(0,5):
    # number는 +1씩 하고
    number += 1
    # 빈 result 변수를 만든다.
    result = ''
    # 이중 for문을 돌린다
    # (사실 re값은 상관없긴함 단순히 5X5 구조를 만들기 위함과 number +=1을 위함임)
    for idx in range(0,5):
      # 두번째 for문에서 idx가 0일 때를 가정하면
      # 현재 두번째 for문에서 첫번째 바퀴이기 때문에 number = 초기 -1 + 1 = 0인 상태
        if idx == number :
          # idx가 0일때 number도 0으로 같으므로
            result +='#'
          # 바로 result에 '#' 추가
        else:
            result += '+'
          # 그리고 나머지는 result에 '+' 추가
    print(result)
    # 이렇게 첫번째 줄 print
    # 그리고 첫번째 for문이 한 번 더 돌면서 number = 1인 상태로 또 돌린다.
    # 이렇게 다섯번째 줄 까지 print하면 완성
```



### 2025. N줄 덧셈

> 1부터 주어진 숫자만큼 모두 더한 값을 출력하시오.
>
> 단, 주어질 숫자는 10000을 넘지 않는다.
>
> 
> **[예제]**
>
> 주어진 숫자가 10 일 경우 출력해야 할 정답은,
>
> 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55



```python
# number값 input값 받고
number = int(input())

# 초기 result는 0으로 설정
result = 0
# 1부터 number까지 다 더해야 하므로 range로 표현
for i in range(1, number+1):
    result += i
 
print(result)
```



### 1938. 아주 간단한 계산기

> 두 개의 자연수를 입력받아 사칙연산을 수행하는 프로그램을 작성하라.
>
>  
>
> **[****제약 사항]**
>
> \1. 두 개의 자연수 a, b는 1부터 9까지의 자연수이다. (1 ≤ a, b ≤ 9)
>
> \2. 사칙연산 + , - , * , / 순서로 연산한 결과를 출력한다.
>
> \3. 나누기 연산의 결과에서 소수점 이하의 숫자는 버린다.
>
>  
>
> **[****입력]**
>
> 입력으로 두 개의 자연수 a, b가 빈 칸을 두고 주어진다.
>
>  
>
> **[****출력]**
>
> 사칙연산의 결과를 각 줄에 순서대로 출력한다.
>
> 입력
>
> 8 3
>
> 출력
>
> 11
> 5
> 24
> 2



```python
# number값을 받는다.
# 중간 스페이스바로 input값을 나눈다고 했으니 split사용
# list로 변환해야 인덱싱하기 좋을 것 같으니 마지막에 list로 형변환
number = list(map(int, input().split()))

# number에 list형으로 들어있는 값을 인덱싱하여
a = number[0]
b = number[1]

# 계산과 동시에 프린트
print(a+b)
print(a-b)
print(a*b)
print(a//b)
```



### 1933. 간단한 N의 약수

> 입력으로 1개의 정수 N 이 주어진다.
>
> 정수 N 의 약수를 오름차순으로 출력하는 프로그램을 작성하라.
>  
>
> **[****제약사항]**
>
> N은 1이상 1,000이하의 정수이다. (1 ≤ N ≤ 1,000)
>  
>
> **[입력]**
>
> 입력으로 정수 N 이 주어진다.
>
> 
> **[****출력]**
>
> 정수 N 의 모든 약수를 오름차순으로 출력한다.
>
> 입력
>
> 10
>
> 출력
>
> 1 2 5 10



```python
number = int(input())

# 빈 str을 만들고
answer = ''

# 1~number까지 for문 돌리며
for i in range(1, number+1):
    # 만약 number가 i로 (1~number까지 차례로 들어가며) 나눠 떨어지면
    if number % i == 0:
        # answer에 스트링화하여 i 추가
        answer += str(i)
        # 빈 칸이 필요하므로 빈 칸 추가
        answer+=' '

print(answer)
```



### 1936. 1대1 가위바위보

> A와 B가 가위바위보를 하였다.
>
> 가위는 1, 바위는 2, 보는 3으로 표현되며 A와 B가 무엇을 냈는지 입력으로 주어진다.
>
> A와 B중에 누가 이겼는지 판별해보자. 단, 비기는 경우는 없다.
>
>  
>
> **[****입력]**
>
> 입력으로 A와 B가 무엇을 냈는지 빈 칸을 사이로 주어진다.
>
>  
>  
>
> **[****출력]**
>
> A가 이기면 A, B가 이기면 B를 출력한다.
>
> 입력
>
> 3 2
>
> 출력
>
> A



```python
# 리스트화하여 number값으로 input받고
number = list(map(int, input().split()))

# 좀 노가다긴 하지만.... 6개의 경우의수를 모두 설정해서 해결
if number[0] == 1 and number[1] ==3:
    print('A')
    
if number[0] == 1 and number[1] ==2:
    print('B')
    
if number[0] == 2 and number[1] ==1:
    print('A')

if number[0] == 2 and number[1] ==3:
    print('B')
    
if number[0] == 3 and number[1] ==1:
    print('B')
    
if number[0] == 3 and number[1] ==2:
    print('A')
```



### 2019. 더블더블

> 1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.
>
> 주어질 숫자는 30을 넘지 않는다.
>
> 입력
>
> 8
>
> 출력
>
> 1 2  4 8 16 32 64 128 256



```python
number = int(input())

answer = ''
# 0~number까지 for문 돌리면서 왜 0부터 ? 2에0승 즉 1도 필요하므로
for i in range(0, number+1):
    # answer에 2에n승을 차례로 추가
    answer += str(2**i)
    # 빈 칸도 필요하므로 추가
    answer += ' '
    
print(answer)
```



### 1545. 거꾸로 출력해 보아요

> 주어진 숫자부터 0까지 순서대로 찍어보세요
>
> 아래는 입력된 숫자가 N일 때 거꾸로 출력하는 예시입니다
>
> 입력
>
> 8
>
> 출력
>
> 8 7 6 5 4 3 2 1 0



```python
number = int(input())
answer = ''
# 받은 number부터 0까지 역으로 for문 돌린다
for i in range(number, -1, -1):
    # 빈스트링에 추가
    answer += str(i)
    # 빈 칸도 추가
    answer += ' '
    
    
print(answer)
```