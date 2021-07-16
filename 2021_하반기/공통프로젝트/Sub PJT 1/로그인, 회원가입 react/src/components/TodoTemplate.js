import React from 'react';
import './TodoTemplate.css';
import { connect } from 'react-redux';

function TodoTemplate({ props, children }) {
  return (
    <div>
      <div className="TemplateBlock">
        {/* <h1> { props.userInfo.username }님 안녕하세요 </h1> */}
        { children }
      </div>
      {/* TodoTemplat에 자식컴포넌트가 생기면 TemplateBlock 사이에 넣어라 */}
    </div>

  )
}

function state를props화(state) {
  return {
    state : state.createReducer,
    alert열렸니 : state.alertReducer,
    // userInfo : state.userReducer
  }
}

export default connect(state를props화)(TodoTemplate);

