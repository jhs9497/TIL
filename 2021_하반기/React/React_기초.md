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



## 프로젝트 생성 & 부트스트랩 설치!

yarn이 더 빠름!

- 설치 : npm install --global yarn
- web 실행 : yarn start
- 부트스트랩 설치
  - react bootstrap 검색
  - npm install react-bootstrap bootstrap@4.6.0  / npm install 대신 yarn add 가능 더 빠름!
  - react bootstrap 사이트의 CSS link 태그를 public - index.html에 복붙 (조금 더 안정적임)
  - django나 vue에서 하듯이 react-bootstrap 사이트 통해 원하는 컴포넌트 가져다가 쓰면됨!
  - or index.js에 import "bootstrap/dis/css/bootstrap.min.css" 해주기



## 이미지 넣기

App.css 

css 안에

background-image : url('./background.jpg') 라 입력!

src폴더에 넣어야 손쉽게 이미지 업로드 가능



## 데이터 따로 보관하기

```javascript
// 파일을 쪼갤 때 활용하는 import/export

// 보내는 파일에서
export default + 단일변수 or {변수1, }

ex) var name = 'Kim';

export default name -> Kim이라는 데이터 송출

// 받는 파일에서
import name from './data.js' // 이제 App.js에서 name이란 이름으로 쓸 수 있음!
import { name, name2 } from '.data.js'


// src 폴더 안에 data.js 라는 파일을 추가한다

export default [
  {
    id : 0,
    title : "White and Black",
    content : "Born in France",
    price : 120000
  },

  {
    id : 1,
    title : "Red Knit",
    content : "Born in Seoul",
    price : 110000
  },

  {
    id : 2,
    title : "Grey Yordan",
    content : "Born in the States",
    price : 130000
  }
]

// 이런식으로 데이터 정립


// App.js

import React, {useState} from 'react';
```



## 상품 반복문 + 컴포넌트로 정렬하기

```javascript
<div className="container">
    <div className="row">
        {
        shoes.map(function(value, i){
            return <ShoesInfo shoes={shoes[i]} i={i} key={i}/>
        	})
        }
            
</div>
	</div>



// 컴포넌트화 그 중 이미지 태그 변수화

function ShoesInfo (props) {
  return (
    <div className="col-md-4">
      <img src={ 'https://codingapple1.github.io/shop/shoes' + (props.i + 1) + '.jpg' } width="100%" />
      <h4>{ props.shoes.title }</h4>
      <p>{ props.shoes.content }</p>
      <p>{ props.shoes.price }원</p>
    </div> 
  )
}


```



## 셋팅과 기본 라우팅

- react-router-dom 라이브러리 사용
- 터미널에 yarn add react-router-dom

### index.js

```javascript
import { BrowserRouter } from 'react-router-dom';

// BrowserRouter 대신에 HashRouter도 사용 가능
// HashRouter가 더 안전하긴 함! BrowserRouter와 다르게 서버한테 요청 절대 X 

ReactDOM.render(
  <React.StrictMode>
    <BrowserRouter>   // BrowserRouter 추가
      <App />
    </BrowserRouter>
  </React.StrictMode>,
  document.getElementById('root')
);
```



### App.js

```java
import { Link, Route, Switch } from 'react-router-dom';

      <Route exact path="/">  // exact를 해줘야 각각 나옴 
        <div>메인페이지에요</div>
      </Route>
      <Route path="/detail">
        <Detail/>
      </Route>
```



### detail.js 따로 만들기

```javascript
import React, { useState } from 'react';
import Detail from './Detail.js';

function Detail() {
  return (
    <div className="container">
      <div className="row">
        <div className="col-md-6">
          <img src="https://codingapple1.github.io/shop/shoes1.jpg" width="100%" />
        </div>
        <div className="col-md-6 mt-4">
          <h4 className="pt-5">상품명</h4>
          <p>상품설명</p>
          <p>120000원</p>
          <button className="btn btn-danger">주문하기</button> 
        </div>
      </div>
    </div> 
  )
}

export default Detail;
```



## Router 버튼 만들기

```javascript
<Nav.Link><Link to="/">Home</Link></Nav.Link> 
<Nav.Link><Link to="/detail">Detail</Link></Nav.Link>
```



### useHistory라는 훅 이용해서 뒤로가기 버튼 만들기

```javascript
import { useHistory } from 'react-router-dom';

let history = useHistory(); // history라는 오브젝트는 나의 방문기록이 다 담겨있다!

<button className="btn btn-success" onClick={()=>{
    history.goBack();
}}>뒤로가기</button> 

history.push('/') -> 특정경로로 이동

```



## Switch

react 라우터는 주소가 중복되면 다 가져오는데

Switch로 전체 라우터를 감싸면 상위 1개만 보여줌!

또 <Route path="/:id"> 이게 의미하는 바는 /뒤에 문자열 어떤것이든! 이란 뜻임



## styled-components

- yarn add styled-components
- 컴포넌트가 많아질 때 사용! 클래스 너무 많아지고 CSS 난무해서 중복될까봐,,

```javascript
// Detail.js

import styled from 'styled-components';

let 박스 = styled.div`
  padding : 20px;
`;

let 제목 = styled.h4`
  font-size : 25px;
  color : ${ props => props.색상 } // 글color를 가변적으로 가져가고 싶을 때
`;

// 똑같이
<박스>
  <제목 색상={'red'} >ㅎㅇㅎㅇㅎㅇㅎㅇ</제목>
</박스>// 이런식으로 사용
```



## Sass 문법 정리

- 설치 : yarn add node-sass
- css를 조금 더 프로그래밍 언어스럽게 작성가능한 Preproccesor

```javascript
// Detail.scss
$메인칼라 : #ffff00;

.Yellow {
  color: $메인칼라;
}

div.container {
  h4 {
    color: blue;
  }
  p {
    color: green;
  }
}

.my-alert {
  background: white;
  padding: 15px;
  border-radius: 5px;
  max-width: 500px;
  width: 100%;
  margin: auto;
}

.my-alert-2 {
  @extend .my-alert;
  background: yellowgreen;  // my-alert랑 다 똑같은데 background만 다르게!
}

@mixin 함수() {
  background: white;
  padding: 15px;
  border-radius: 5px;
  max-width: 500px;
  width: 100%;          // 이 설정을 함수화해서 사용도 가능
  margin: auto;
}

.my-alert-3 {  
  @include 함수() 
}


// 여기에 SASS 문법 작성가능
// 자동으로 컴파일링해줌


// Detail.js
import './Detail.scss';
```



## useEffect 훅 / 2초 뒤에 alert창 없애기

```javascript
// Detail.js

// 컴포넌트가 mount 되었을때, 컴포넌트가 update될 때 특정 코드를 실행할 수 있음

  useEffect(()=>{
    setTimeout(()=>{
		alert변경(false)
    }, 2000)
  });  // 2초 후에 특정 함수를 실행하게 해주세요!

  let [alert, alert변경] = useState(true);


{
    alert === true
        ? <div className="my-alert">
        <p>재고가 얼마 남지 않았습니다.</p>
        </div>
    : null
}


  // useEffect(()=>{
  //   return function 어쩌구(){
  //     실행할코드 // Detail이란 컴포넌트가 사라질때 실행!
  //   }
  // });
```



## useEffect 조건

![image-20210707020503223](image-20210707020503223.png)

useEffect는 update될 때도 실행되므로 input값에 입력할때마다 실행됨을 볼 수 있음



```javascript
  useEffect(()=>{
    setTimeout(()=>{
      alert변경(false)
    }, 2000);
  }, [alert]); // 맨 아래 대괄호 안에 조건!을 넣을 수 있음 alert라는 state가 변경이 될때만 실행하자! 여러개도 가능!


  useEffect(()=>{
    setTimeout(()=>{
      alert변경(false)
    }, 2000);
  }, []); // 조건에 빈 리스트 넣으면 useEffect를 딱 첫 페이지 실행됐을때만 사용가능하게!


// 라스트!

  useEffect(()=>{
    let 타이머 = setTimeout(()=>{
      alert변경(false)
    }, 2000);
    return ()=>{ clearTimeout(타이머) }  // detail 페이지 들어가자마자 뒤로가기를 누르면 버그가 생길 수 있으므로 안정적으로 setTimeout 구현을 위해 사용
  }, [alert]);
```



## Ajax

- 서버에 새로고침없이 요청을 할 수 있게 도와줌!
- 요청은 여러 종류가 있는데
  - GET 요청 : 주소창에 URL 때려박는 요청 / 특정 페이지 / 자료 읽기
  - POST 요청 : 서버로 중요 정보 전달
  - 둘 다 요청할때 새로고침 됨! 별로임!
- Ajax는 axios, fetch() 중 하나 쓰면 됨! / 우리는 axios ㄱㄱ

1. 터미널창에 yarn add axios
2. import axios from 'axios';
3. vue랑 똑같네!



## Context API

- 하위컴포넌트들이 props 없이도 부모의 값을 공유 및 사용 가능

```javascript
// 1. App.js function App 위에다가

let 재고context = React.createContext();

// 2. 공유하고싶은 컴포넌트를 태그로 감싸준다.
// ex) row라는 컴포넌트와 shoesInfo라는 컴포넌트 모두에게서 재고라는 값을 공유

            <재고context.Provider value={재고}>

            <div className="row">
              {
                shoes.map(function(value, i){
                  return <ShoesInfo shoes={shoes[i]} i={i} key={i}/>
                })
              }
            </div>

            </재고context.Provider>


```



## Tab기능 만들기

1. 몇번째 버튼 눌렀는지를 state로 저장해둠
2. state에 따라 UI 보이게 안보이게



```javascript
      <Nav className="mt-5" variant="tabs" defaultActiveKey="link-0"> // defalut는 초기화면
        <Nav.Item>
          <Nav.Link eventKey="link-0">Active</Nav.Link>
        </Nav.Item>
        <Nav.Item>
          <Nav.Link eventKey="link-1">Option 2</Nav.Link>
        </Nav.Item>
      </Nav>


	if/else가 아니라 여러개의 if문이 필요하므로 component화 한다.
    
    <TabContetn 누른탭={누른탭}/>
        
        
        
function TabContent(props){

  if (props.누른탭 === 0) {
    return <div>000번째 탭</div>
  } else if (props.누른탭 === 1) {
    return <div>111번째 탭</div>
  } else if (props.누른탭 === 2 ) {
    return <div>222번째 탭</div>
  }
}
```



## Tab에 애니메이션 추가

- yarn add react-transition-group

```react
import { SwitchTransition, CSSTransition } from "react-transition-group";


// 원하는 내용 감싸기
let[탭스위치, 탭스위치변경] = useState(false);


<CSSTransition in={탭스위치} classNames="wow" timeout={500}> 스위치, 애니메이션이름, 지속시간
  <TabContent 누른탭={누른탭}/>
</CSSTransition>



// Detail.css  
.wow-enter {    // wow라는 애니메이션이 시작할때 설정
  opacity: 0;
}
.wow-enter-active {   // wow라는 애니메이션이 동작중일때 설정
  opacity: 1;
  transition: all 500ms;
}
```





## Redux

- 설치 : yarn add redux react-redux
- 컴포넌트 많아지면 props 힘들어지니깐 props없이 쓰려고!
  1. Provider import 해오기
  2. 내가 state값 공유를 원하는 컴포넌트를 다 감싸기
     - 그러면 해당 컴포넌트와 그 안에 있는 모든 HTML, 컴포넌트들은 전부 state를 직접! props전송 없이 사용가능함
  3. redux에서 state를 하나 만드려면 createStore()함수 사용
  4. Provider에 만든 state를 props처럼 state이름={state이름} 해주면됨
  5. 원하는 컴포넌트.js밑에 connect()를 통한 function하나를 만들어줌
  6. props가져오고 props.블라블라로 데이터 바인딩 가능!



```react
// index.js

import { Provider } from 'react-redux';
import { createStore } from 'redux';

let store = createStore(()=>{ return [{ id : 0, name : '멋진신발', quan : 2 }] });

// BrowserRouter 대신에 HashRouter도 사용 가능
// HashRouter가 더 안전하긴 함! BrowserRouter와 다르게 서버한테 요청 절대 X 

ReactDOM.render(
  <React.StrictMode>
    <BrowserRouter>
      <Provider store={store}>
        {/* // Provider 사이에 있는 컴포넌트 들은 store를 모두 공유할 수 있음 */}
        <App />
      </Provider>
    </BrowserRouter>
  </React.StrictMode>,
  document.getElementById('root')
);



// cart.js

import { div } from 'prelude-ls';
import React from 'react';
import {Table} from 'react-bootstrap';
import { connect } from 'react-redux';

function Cart(props){
  return (
    <div>
      <Table responsive>
        <thead>
          <tr>
            <th>#</th>
            <th>상품명</th>
            <th>수량</th>
            <th>변경</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>1</td>
            <td>{ props.state[0].name }</td>
            <td>Table cell</td>
            <td>Table cell</td>
          </tr>
        </tbody>
      </Table>
    </div>
  )
}

function state를props화(state){   // store에 있던 데이터를 state라는 이름으로 가져오는 함수
                          // redux store 데이터 가져와서 props화 해주는 함수
  return {
    state : state
  }
}


export default connect(state를props화)(Cart)





## Redux 데이터 수정하기

- 데이터관리 용이함! 이것이 redux를 쓰는 또 하나의 이유
- 데이터가 어디서 에러가 났을때 어떤 부분에서 에러나는지 찾기 쉬워짐!
  1. state 데이터의 수정방법을 미리 정의한다.
  2. 수정된 state를 퉤 뱉는 reducer라는 함수를 정의
- 다만 만약 컴포넌트 하나에서만 쓰는건 굳이 리덕스쓰지말고 해당 컴포넌트에 useState로 쓰는게 낫다!

​```react
// index.js
// 데이터 수정방법 미리 정의하기

let 초기state = [
  { id : 0, name : '멋진신발', quan : 2 },
  { id : 1, name : '호우신발', quan : 99 },
  { id : 2, name : '메시신발', quan : 1 },
] 

function reducer(state = 초기state, 액션){   // state = 블라블라 를 통해 기본값 설정 가능
  if ( 액션.type === '수량증가' ){  // 데이터가 수정되는 조건
    
    let 수정된state = [...state];
    수정된state[0].quan++;
    return 수정된state

  } else if ( 액션.type ==='수량감소' ){

    if ( state[0].quan === 0 ) {
      return state
    } else {
      let 수정된state = [...state];
      수정된state[0].quan--;
      // 수정된state[0].quan = state[0].quan - 1
      return 수정된state
    }


  } else {
    
    return state
  }
}

let store = createStore(reducer);

// cart.js 에서 사용하기

<button onClick={()=>{ props.dispatch({ type : '수량증가' }) }}>+</button>
<button onClick={()=>{ props.dispatch({ type : '수량감소' }) }}>-</button>
```



## reducer 여러개 만들기

```react
// index.js
import { combineReducers, createStore } from 'redux';

let store = createStore(combineReducers({reducer, reducer2})); 
// 내가 만든 모든 reducer 넣어주는 문법 import해야함


// cart.js
function state를props화(state){   // store에 있던 데이터를 state라는 이름으로 가져오는 함수
                          // redux store 데이터 가져와서 props화 해주는 함수
                          // reducer가 2개면 state에 reducer가 2개가 넘어옴!
  return {
    state : state.reducer,
    alert열렸니 : state.reducer2,
  }
}

3


```



## dispatch할 때 데이터 실어 보내기

```react
props.dispatch({ type : '항목추가', payload : {id:2, name:'새로운상품', quan:1} });
```





## 성능잡기 1 / lazy loading / React devtools



1. 함수나 오브젝트는 변수를 선언해서 사용할 것! 메모리 할당 때문 
   - 오.. 모던자바스크립트 내용! 
   - 변수를 사용하지 않으면 페이지 재렌더링할때 할 때 마다 메모리를 재할당 해야하는데 변수를 통해 이름을 지정해주면 그런 불필요한 메모리 할당 문제가 일어나지 않음!

```react
// 스타일 먹일 때

var style = { color : 'red' }

<tr style={ style }></tr>

// 애니메이션 줄 때
margin, width, padding 등 이런 레이아웃 잡는 속성들은 애니메이션 막주지말고
되도록이면 transform ㄱㄱㄱㄱㄱ transform이 무엇 ?
    
// App.js
컴포넌트 import할 때 우선 자바스크립트는 위에서부터 하나씩 다 읽음 컴포넌트 많으면 좀 힘들어할 수 있음
각 컴포넌트가 필요해질 때 import하라고 명령할 수 있음! 
import { lazy, Suspense } from 'react';

import Detail from './Detail.js'; // 이 구문을 아래로 변경!
let Detail = lazy(()=> import('./Detail.js') );

// 무조건 다 import해오는게 아니라 Detail 컴포넌트가 필요해질 때 import해옴 ! 성능 upup

// 마지막으로 Detail컴포넌트를 <Suspense> 태그로 감싸주면 완 성 !
<Suspense fallback={<div>로딩중이에요</div>}>   // 인터넷환경이 느릴경우 로딩중에 띄울 화면
    <Detail/>
</Suspense>
    
```

