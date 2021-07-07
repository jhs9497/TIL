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

```react
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



```



## dispatch할 때 데이터 실어 보내기

```react
props.dispatch({ type : '항목추가', payload : {id:2, name:'새로운상품', quan:1} });
```