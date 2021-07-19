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
          {
            props.state.map((value,i)=>{
              return (
                <tr key={i}>
                  <td>{ value.id }</td>
                  <td>{ value.name }</td>
                  <td>{ value.quan }</td>
                  <td>
                    <button onClick={()=>{ props.dispatch({ type : '수량증가', payload : value.id }) }}>+</button>
                    <button onClick={()=>{ props.dispatch({ type : '수량감소', payload : value.id }) }}>-</button>
                  </td>
                </tr>
              )
            })
          }
        </tbody>
      </Table>
      { props.alert열렸니 === true
        ? <div className="my-alert">
          <p>지금 구매하시면 신규할인 20%</p>
          <button onClick={()=>{ props.dispatch({ type : 'alert닫기'}) }}>닫기</button>
        </div>
        : null
      }


    </div>
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


export default connect(state를props화)(Cart)