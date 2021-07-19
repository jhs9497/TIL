## React

- node.js 최신버전 설치 -> why? create-react-app이라는 라이브러리를 사용하기위해서!!!
- 리액트 설치: npx create-react-app blog(이름)
- 사이트 열기 : npm start
- index.js는 App.js안의 div속 내용들을 index.html로 보내준다.
- bootstrap 깔기 -> npm install bootstrap --save
- cd '앱 이름' // 폴더 이동하기
- react, redux, react-router, webpack, contextAPI?



## JSX

- HTML이랑 비슷한데 class 대신 className
- 데이터바인딩(데이터를 HTML에 꽂아넣는 것)을 하기 매우 쉽다!!
- {} 중괄호 안에 변수 넣는걸로 끝! 심지어 함수도 가능... { 함수() } 이런식으로!
- 이미지는 import로 가져오고 그 변수명을 img 태그 안에 {}중괄호 이용
- style 개별 부여시엔 중괄호 안에 오브젝트 형식으로! & 카멜 케이스

```javascript
<div style={ { color : 'blue', fontSize : '30px' } }>개발 Blog</div>
```



## State

```javascript
import React, {useState} from 'react';

function App() {
    
    let[글제목, 글제목변경] = useState('남자 코트 추천'); # 요렇게 쓰면 [a,b] 이런 배열이 생김
    						  # a에는 '남자 코트 추천', b에는 수정할 함수 들어간다.
}
```



state는 

1. 변수대신 쓰는 데이터 저장공간
2. useState()를 이용해 만들어야함
3. [state데이터, state데이터 변경 함수]
4. 문자, 숫자,  array, object 다 저장 가능
5. react를 웹App처럼 동작하게 만들고 싶어서 사용!
6. state는 변경이 되면 HTML이 **자동으로 재렌더링** 된다! -> 새로고침안해도 됨!



## 이벤트 리스너

*/\* eslint-disable \*/* *// 노랑이 안뜨게!*



```react
 <span onClikc={ 함수() }> 👍 </span>
 <span onClikc={ ()=>{} }> 👍 </span>

let [따봉, 따봉변경] = useState(0);

<h3>{ 글제목[0] } <span onClick={ ()=>{ 따봉변경(따봉+1) } }>👍</span> { 따봉 } </h3>

<button onClick={()=>{글제목변경([] = ['여자 코트 추천', '강남 우동 맛집', '회기 파전 맛집'])}}>제목 바꿔주기</button>
```



## Array인 State 변경하기

```react
function 제목변경() {
  var newArray = [...글제목];    // 딥카피!!!!!
  newArray[0] = '여자 코트 추천';
  글제목변경( newArray ); // 글제목변경()은 데이터를 아예 갈아치우는 함수!
}

<button onClick={ 제목변경 }>제목 바꿔주기</button>
```



## Modal 창으로 띄우는 상세페이지 (컴포넌트 만들기)

```javascript
// App.css

.modal {
  margin-top: 20px;
  padding: 20px;
  background: #eee;
}

// App.js
// HTML 줄여서 쓸 수 있는 방법 

// before

<div className='modal'>
    <h2>제목</h2>
    <p>날짜</p>
    <p>상세내용</p>
</div>

// after
// component로 만들기!
// funtion App 바깥에다가!

function Modal() { // 이름은 대문자로 만든다
  return (
    <div className='modal'>  // return()안에 있는건 태그 하나로 묶어야함!
      					     // 정 div쓰기 싫으면 <> </>로 묶을 수 있음
      <h2>제목</h2>
      <p>날짜</p>
      <p>상세내용</p>
  	</div>
  )
}
// 만들고

// function App 안에다가
<Modal></Modal>
// 이런식으로 사용하기
```



## 동작하는 모달창 만들기

```javascript

let [modal, modal변경] = useState(false);  // 우선 스테이트 만들기

<div className='list'>
    <h3 onClick={ () => { modal === false ? modal변경(true) : modal변경(false)} }>내가 만든 모달 show</h3>
	<h3 onClick={ () => { modal변경(!modal) } }>더 간단한 방법</h3>
	<p>2월 17일 발행</p>
	<hr/>
</div>


{
   // 1 < 3 
   // ? console.log('맞아요') 
   // : console.log('틀려요')  
   // if 3항연산자를 쓰는 이유 : 문법적으로 {}안에 일단 if함수가 들어갈 수 없음
   modal === true // modal이란 state가 true면!
   ? <Modal></Modal>
   : null // 텅빈 HTML이란 뜻
}
```



## 반복문

```javascript
// for문을 이용한 일반 반복문

function 반복된UI() {
    
    var 어레이 = [];
    for (var i = 0; i < 3; i++){
      어레이.push(<div>안녕</div>);
    }
    return 어레이
}

// fucntion App 안에서!

{ 반복된UI() }


// But JSX 중괄호 내에 for문 못넣음..! 변수명, 함수명만 가능
// map()이라는 함수쓰기! 
var 어레이 = [2,3,4];

var 뉴어레이 = 어레이.map(function(a){
    return a * 2
});

// 적용
      {
        글제목.map(function(value){ // value가 글제목이란 array안에 있던 요소들
          return ( // 보통 괄호로 묶어줌
          <div className="list">
            <h3> { value } </h3>
            <p> .map이용해서 반복문으로 돌리는중 </p>
            <hr/>
          </div>  
          )
        })
      }
```



## props

```javascript
// 현재 App -> 부모 컴포넌트, Modal -> 자식 컴포넌트이다.
// 부모 -> 자식으로 데이터전송 가능! (props로 전송


// step 1

{
  modal === true // modal이란 state가 true면!
  ? <Modal 글제목={글제목}></Modal> // 변수={전송할 state}
  : null // 텅빈 HTML이란 뜻
}

// step 2
function Modal(props) { // 부모에게서 전달받은 props는 props에 다 들어있음
  return (
    <div className='modal'>
      <h2>{ props.글제목[0] }</h2> // props안에 들어있음!
      <p>날짜</p>
      <p>상세내용</p>
  </div>
  )
}
```



## 제목을 누를때 각각 다른 모달창 뜨게 하기

```javascript
let [누른제목, 누른제목변경] = useState(0);

      {
        modal === true // modal이란 state가 true면!
        ? <Modal 글제목={글제목} 누른제목={누른제목}></Modal> // 변수={전송할 state}
        : null // 텅빈 HTML이란 뜻
      }


      {
        글제목.map(function(value, i){ // value가 글제목이란 array안에 있던 요소들
          return ( // 보통 괄호로 묶어줌
          <div className="list" key={i}>  // key를 써줘야 콘솔창에 워닝이 안뜸
            <h3 onClick={ ()=>{ 누른제목변경(i)} }> { value } </h3>
            <p> .map이용해서 반복문으로 돌리는중 </p>
            <hr/>
          </div>  
          )
        })
      }
```



## input data 바인딩

```javascript
// state
let [입력값, 입력값변경] = useState('');

// App
// react에서 onInput이랑 onChange는 같은 기능을 함!

<input onChange={ (e)=>{ 입력값변경(e.target.value) } } />
<h3>{ 입력값 }</h3>
// e.target.value 자바스크립트 문법!
```





## 글발행기능

```javascript
// state
let [입력값, 입력값변경] = useState('');

function 글제목추가() {
  var newArray = [...글제목];
  // newArray.push(입력값) // 뒤에 추가
  newArray.unshift(입력값) // 앞에 추가
  글제목변경( newArray );
  입력값변경('')
}


// App
      <div className='publish'>
        <input onChange={ (e)=> { 입력값변경(e.target.value) } }/>
        <button onClick ={ 글제목추가 }>저장</button>
      </div>

// css

.publish{
  margin-top: 30px;
  margin-bottom: 30px;
}
.publish input {
  padding: 10px;
  font-size: 16px;
  border-radius: 5px;
  width: 80%;
  border: 1px solid grey;
}
.publish button {
  display: block;
  margin: auto;
  margin-top: 10px;
}
```



