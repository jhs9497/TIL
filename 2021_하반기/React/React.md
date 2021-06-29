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

