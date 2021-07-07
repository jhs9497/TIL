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

