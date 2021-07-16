import React, { useEffect, useState, useContext } from 'react';
import { propTypes } from 'react-bootstrap/esm/Image';
import { useHistory, useParams } from 'react-router-dom';
import { Nav } from 'react-bootstrap';
import styled from 'styled-components';
import './Detail.css';
import {재고context} from './App.js';
import { connect } from 'react-redux';

import { SwitchTransition, CSSTransition } from "react-transition-group";



let 박스 = styled.div`
  padding : 20px;
`;

let 제목 = styled.h4`
  font-size : 25px;
  color : ${ props => props.색상 }
`;


function Detail(props) {

  let [alert, alert변경] = useState(true);
  let [input, input변경] = useState('');

  let[누른탭, 누른탭변경] = useState(0);

  let[탭스위치, 탭스위치변경] = useState(false);

  let 재고 = useContext(재고context)

  useEffect(()=>{
    let 타이머 = setTimeout(()=>{
      alert변경(false)
    }, 2000);
    return ()=>{ clearTimeout(타이머) }
  }, [alert]);

  let { id } = useParams();  // :id 자리에 있던 숫자 변수화
  let 찾은상품 = props.shoes.find(function(상품){
    return 상품.id == id
  });
  let history = useHistory(); // history라는 오브젝트는 나의 방문기록이 다 담겨있다!

  return (
    <div className="container">
      <박스>
        <제목 색상={'red'} >ㅎㅇㅎㅇㅎㅇㅎㅇ</제목>
        <제목 >ㅎㅇㅎㅇㅎㅇㅎㅇ</제목>
      </박스>

      <p>{ input }</p>
      <p><input onChange={(e)=>{ input변경(e.target.value) }}/></p>

      {
        alert === true
        ? <div className="my-alert">
            <p>재고가 얼마 남지 않았습니다.</p>
          </div>
        : null
      }


      <div className="row">
        <div className="col-md-6">
          <img src='https://codingapple1.github.io/shop/shoes1.jpg' width="100%" />
        </div>
        <div className="col-md-6 mt-4">
          <h4 className="pt-5">{찾은상품.title}</h4>
          <p>{찾은상품.content}</p>
          <p>{찾은상품.price}원</p>

          <Info 재고={재고}></Info>

          <button className="btn btn-danger" onClick={ () => { 

            props.재고변경([9,10,12]) 
            props.dispatch({ type : '항목추가', payload : {id:찾은상품.id, name:찾은상품.title, quan:1 }});
            history.push('/cart');

          }}>주문하기</button> 
          <button className="btn btn-success" onClick={()=>{
            history.goBack();
          }}>뒤로가기</button> 
        </div>
      </div>

      <Nav className="mt-5" variant="tabs" defaultActiveKey="link-0">
        <Nav.Item>
          <Nav.Link eventKey="link-0" onClick={()=>{ 탭스위치변경(false); 누른탭변경(0) }}>Active</Nav.Link>
        </Nav.Item>
        <Nav.Item>
          <Nav.Link eventKey="link-1" onClick={()=>{ 탭스위치변경(false); 누른탭변경(1) }}>Option 2</Nav.Link>
        </Nav.Item>
        <Nav.Item>
          <Nav.Link eventKey="link-2" onClick={()=>{ 탭스위치변경(false); 누른탭변경(2) }}>Option 2</Nav.Link>
        </Nav.Item>
      </Nav>

      <CSSTransition in={탭스위치} classNames="wow" timeout={500}>
        <TabContent 누른탭={누른탭} 탭스위치변경={탭스위치변경}/>
      </CSSTransition>

    </div> 
  )
}

function TabContent(props){

  useEffect(()=>{
    props.탭스위치변경(true);
  });

  if (props.누른탭 === 0) {
    return <div>000번째 탭</div>
  } else if (props.누른탭 === 1) {
    return <div>111번째 탭</div>
  } else if (props.누른탭 === 2 ) {
    return <div>222번째 탭</div>
  }
}



function Info(props){
  return (
    <p>재고 : {props.재고[0]} </p>
  )
}

function state를props화(state){   // store에 있던 데이터를 state라는 이름으로 가져오는 함수
  // redux store 데이터 가져와서 props화 해주는 함수
  // reducer가 2개면 state에 reducer가 2개가 넘어옴!
return {
state : state.reducer,
alert열렸니 : state.reducer2,
}
}


export default connect(state를props화)(Detail)