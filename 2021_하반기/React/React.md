## React

- node.js 최신버전 설치 -> why? create-react-app이라는 라이브러리를 사용하기위해서!
- 리액트 설치: npx create-react-app blog(이름)
- 사이트 열기 : npm start
- index.js는 App.js안의 div속 내용들을 index.html로 보내준다.
- bootstrap 깔기 -> npm install bootstrap --save
- cd '앱 이름' // 폴더 이동하기
- react, redux, react-router, webpack, contextAPI? 영어강의 듣지말기!



## JSX

- HTML이랑 비슷한데 class 대신 className
- 데이터바인딩(데이터를 HTML에 꽂아넣는 것)을 하기 매우 쉽다!
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
  글제목변경( newArray );
}

<button onClick={ 제목변경 }>제목 바꿔주기</button>
```

