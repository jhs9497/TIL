# 1. 변수



### 변수란 무엇이고 왜 사용하는가?

변수는 하나의 값을 저장하기 위해 확보한 메모리 공간 자체, 또는 그 메모리공간을 식별하기 위해 붙인 이름이다. 개발자가 직접 메모리 주소를 통해 값을 저장하고 치환할 경우 시스템 오류가 날 수 있기 때문이다. 변수(식별자)는 값이 아니라 메모리 주소를 기억하고 있다. 



![img](https://blog.kakaocdn.net/dn/UFuwu/btq9Y6EjoI8/39PKV3aVzvbM0kFCaJqskK/img.png)



 

### 키워드란 ?

자바스크립트 엔진은 키워드를 만나면 자신이 수행해야 될 약속된 동작을 수행한다.

키워드 ex) var, let, const, function, class

var라는 키워드의 경우 var 뒤에 오는 변수이름으로 새로운 변수를 생성하고, 값을 지정하지 않은 경우 초기값을 undefined로 설정하는 '약속된 동작'을 수행한다.

 

 

### 변수 호이스팅

자바스크립트는 기본적으로 코드를 인터프리터에 의해 한 줄씩 순차적으로 실행되는 동기적인 방식을 취하고 있다. 하지만 변수선언의 경우 (값을 할당한 상태는 아님) 런타임이 아니라 그 이전 단계에서 먼저 실행되기 때문에 변수를 선언한 부분보다 위쪽에서 console을 찍어도 var 변수의 초기값인 defined가 출력되는 것을 볼 수 있다. 



![img](https://blog.kakaocdn.net/dn/cJMpKM/btq9Y5MbfTQ/9X34vSV74nocKdnw4pq7Kk/img.png)



하지만 변수 할당 (값을 넣는 것)은 런타임 도중에 일어나므로 중간에 값을 할당하면 아래와 같은 결과가 나온다.



![img](https://blog.kakaocdn.net/dn/54Hbr/btq91M6a2IM/kONM1oj4U6IcQLupvEt8cK/img.png)



###  

### 자바스크립트 식별자 네이밍 규칙

변수를 명명할 때 프로그램언어 별로 선호하는 명명방식이 있다. 자바스크립트의 경우는 아래와 같다.



![img](https://blog.kakaocdn.net/dn/cPuKcF/btq93oX5Nxt/PLoJmSJ6xEQTdyCm3KeTw1/img.png)





# 2. 표현식과 문



### 표현식

표현식은 값으로 평가될 수 있는 문이다. 즉, 표현식이 평가되면 새로운 값을 생성하거나 기존값을 참조한다. **쉽게 생각해서 값으로 평가될 수 있는 문은 모두 표현식이다. 아래의 문 모두 표현식이다.**



![img](https://blog.kakaocdn.net/dn/bRNBYt/btq9XbsptR6/JuTtfxCNs65RON8U43dgFk/img.png)



 

### 문(statement)

문은 프로그램을 구성하는 기본단위이자 최소 '실행' 단위이다. 최소의 문장이라고 생각하면 좋을 것 같다. 이러한 문의 집합으로 이뤄진 것이 바로 프로그램이며, 문을 작성하고 순서에 맞게 나열하는 것이 프로그래밍이다. 문은 여러개의 token으로 이루어졌다. token이란 문법적인 의미를 가지며, 더 이상 나눌 수 없는 코드의 기본요소를 말한다. 



![img](https://blog.kakaocdn.net/dn/wj0Nd/btq91pQW5MJ/lhMvqzLyYL1U2a1OmQISMk/img.png)