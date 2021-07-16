import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

import { BrowserRouter } from 'react-router-dom';

import { Provider } from 'react-redux';
import { combineReducers, createStore } from 'redux';


let alert초기값 = true;

function reducer2(state = alert초기값, 액션){
  if ( 액션.type === 'alert닫기' ){
    state = !state;
  } return state;
}


let 초기state = [
  { id : 0, name : '멋진신발', quan : 2 },
  { id : 1, name : '호우신발', quan : 99 },
  { id : 2, name : '메시신발', quan : 1 },
];

function reducer(state = 초기state, 액션){   // state = 블라블라 를 통해 기본값 설정 가능
  if ( 액션.type === '항목추가') {

    let found = state.findIndex((a)=>{ return a.id === 액션.payload.id }) 
    // a === 액션.payload.id랑 같으면 그 a값이 남음!

    if (found){

      let copy = [...state];
      copy[found].quan++;
      return copy

    } else {
      let copy = [...state];
      copy.push(액션.payload);
      return copy
    }



  } else if ( 액션.type === '수량증가' ){  // 데이터가 수정되는 조건
    let 수정된state = [...state];
    수정된state[액션.payload].quan++;
    return 수정된state

  } else if ( 액션.type ==='수량감소' ){

    if ( state[액션.payload].quan === 0 ) {
      return state
    } else {
      let 수정된state = [...state];
      수정된state[액션.payload].quan--;
      // 수정된state[0].quan = state[0].quan - 1
      return 수정된state
    }


  } else {
    
    return state
  }
}

let store = createStore(combineReducers({reducer, reducer2})); // 내가 만든 모든 reducer 넣어주는 문법 import해야함



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

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
