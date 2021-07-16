/* eslint-disable */  // 노랑이 안뜨게!

import React, {useState} from 'react';
import logo from './logo.svg';
import './App.css';

function App() {

  let [글제목, 글제목변경] = useState(['남자 코트 추천', '강남 우동 맛집', '회기 파전 맛집']);
  let [따봉, 따봉변경] = useState(0);

  let [modal, modal변경] = useState(false);
  let [누른제목, 누른제목변경] = useState(0);

  let [입력값, 입력값변경] = useState('');

  let posts = '강남 고기 맛집';
  function 함수 (){
    return 100
  }

  function 제목변경() {
    var newArray = [...글제목]; // 딥카피!!
    newArray[0] = '여자 코트 추천';
    // newArray.sort()
    글제목변경( newArray ); // 글제목변경()은 데이터를 아예 갈아치우는 함수!
  }

  function 글제목추가() {
    var newArray = [...글제목];
    // newArray.push(입력값) // 뒤에 추가
    newArray.unshift(입력값) // 앞에 추가
    글제목변경( newArray );
    입력값변경('')
  }

  return (
    <div className="App">
      <div className="black-nav">
        <div style={ { color : 'blue', fontSize : '30px' } }>개발 Blog</div>
      </div>
      <button onClick={ 제목변경 }>제목 바꿔주기</button>
      <div className='list'>
        <h3>{ 글제목[0] } <span onClick={ ()=>{ 따봉변경(따봉+1) } }>👍</span> { 따봉 } </h3>
        <p>2월 17일 발행</p>
        <hr/>
      </div>
      <div className='list'>
        <h3>{ 글제목[1] }</h3>
        <p>2월 17일 발행</p>
        <hr/>
      </div>
      <div className='list'>
        <h3>{ 글제목[1] }</h3>
        <p>2월 17일 발행</p>
        <hr/>
      </div>

      <button onClick={ () => { modal === false ? modal변경(true) : modal변경(false)} }>열고닫기 ver1</button>
      <button onClick={ () => { modal변경(!modal) } }>열고닫기 ver2</button>

      {
        // 1 < 3 
        // ? console.log('맞아요') 
        // : console.log('틀려요')  
        // if 3항연산자를 쓰는 이유 : 문법적으로 {}안에 일단 if함수가 들어갈 수 없음
        modal === true // modal이란 state가 true면!
        ? <Modal 글제목={글제목} 누른제목={누른제목}></Modal> // 변수={전송할 state}
        : null // 텅빈 HTML이란 뜻
      }

      {
        글제목.map(function(value, i){ // value가 글제목이란 array안에 있던 요소들
          return ( // 보통 괄호로 묶어줌
          <div className="list" key={i}>
            <h3 onClick={ ()=>{ 누른제목변경(i), modal변경(!modal) } }> { value } </h3>
            <p> .map이용해서 반복문으로 돌리는중 </p>
            <hr/>
          </div>  
          )
        })
      }

      {/* <input onChange={ (e)=>{ 입력값변경(e.target.value) } } />
      <h3>{ 입력값 }</h3> */}


      <div className='publish'>
        <input onChange={ (e)=> { 입력값변경(e.target.value) } }/>
        <button onClick ={ 글제목추가 }>저장</button>
      </div>
     

    </div>
  );
}

function Modal(props) { // 부모에게서 전달받은 props는 props에 다 들어있음
  return (
    <div className='modal'>
      <h2>{ props.글제목[props.누른제목] }</h2>
      <p>날짜</p>
      <p>상세내용</p>
  </div>
  )
}


export default App;
