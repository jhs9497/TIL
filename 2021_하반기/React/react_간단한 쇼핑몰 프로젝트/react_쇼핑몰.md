## 프로젝트 생성 & 부트스트랩 설치

yarn이 더 빠름!

- 설치 : npm install --global yarn
- web 실행 : yarn start
- 부트스트랩 설치
  - react bootstrap 검색
  - npm install react-bootstrap bootstrap@4.6.0  / npm install 대신 yarn add 가능 더 빠름!
  - react bootstrap 사이트의 CSS link 태그를 public - index.html에 복붙 (조금 더 안정적임)
  - django나 vue에서 하듯이 react-bootstrap 사이트 통해 원하는 컴포넌트 가져다가 쓰면됨!



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

