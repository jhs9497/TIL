# 리액트에서 자주쓰는 if문 작성패턴 5개



## 1. 컴포넌트 안에서 쓰는 if/else

컴포넌트에서 JSX를 조건부로 보여주고 싶은경우 쓴다

자바스크립트 if문은 return ()안의 JSX 내에서는 사용 불가하다.

<div> if (어쩌구) {저쩌구} </div> 이게 안된다는 뜻!

그래서 보통 return + JSX 전체를 뱉는 if문을 작성해 사용한다

```react
function Component() {
    if ( true ) {
        return <p>참이면 보여줄 HTML</p>;
    }
    return null;
}
```





## 2. JSX안에서 쓰는 삼항연산자

그냥 if와는 다르게 JSX안에서도 실행가능하며 조건이 if/else일때 사용한다.

```react
function Component() {
    return (
    <div>
      {
      	1 === 1
        ? <p>첫 줄 조건이 참이면 보여줄 HTML</p>
        : <p>첫 줄 조건이 거짓이면 보여줄 HTML</p>
      }
    </div>
    )
}
```



## 3. && 연산자로 if 역할 대신하기

"만약에 이 변수가 참이면 <p></p>를 이 자리에 뱉고 아니면 null 뱉는 if/else일 경우"

if문을 좀더 쉽게 축약하는 방법

```react
function Component() {
    return (
    <div>
      {
      	1 === 1 && <p>첫 줄 조건이 참이면 보여줄 HTML</p>
      }
    </div>
    )
}
```



## 4. switch / case로 여려개로 중첩된 if문 대체하기



```react
function reducer(state, 액션){
    if (액션.type === '수량증가'){
        return 블라블라
    } else if (액션.type === '수량감소'){
        return 블라블라
    } else {
        return 블라블라
    }
}

위와 같은 중첩 if문을
```



```react
function reducer(state, 액션){
    switch (액션.type) {
        case '수량증가':
            return 블라블라
        case '수량감소':
            return 블라블라
        default :
            return 블라블라
    }
}

요렇게 switch/case문으로 바꿀 수 있음 조금 더 보기 편한듯 ?
```



## 5. 오브젝트 자료형을 응용한 enum



현재 state가 info면 상품정보를

현재 state가 shipping이면 배송정보를

현재 state가 refund면 환불약관을

보여주고 싶은 경우!

if문이 아닌 더 간단한 방법으로 가능

```react
function Component() {
    var 현재상태 = 'info';
    return (
       <div>
         {
           {
             info : <p>상품정보</p>,
             shipping : <p>배송관련</p>,
             refund : <p>환불약관</p>
           }[현재상태]     // <-- object뒤에 [] 이 친구를 통해 "key"값이 현재상태인 자료를 뽑겠다!
         } 
       </div>
    )
}
```

혹은 더 간지나게

```react
var 탭UI = {
    info : <p>상품정보</p>,
    shipping : <p>배송관련</p>,
    refund : <p>환불약관</p>
}

function Component() {
    var 현재상태 = 'info';
    return (
       <div>
         {
           탭UI[현재상태]
         } 
       </div>
    
    )
}
```

