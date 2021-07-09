import styled from 'styled-components';
import { connect } from 'react-redux';
import {useState} from 'react';

const InsertFormPositioner = styled.div`
  width: 100%;
  bottom: 0;
  left: 0;
  position: relative;
`;

const InsertForm = styled.form`
  background: #f8f9fa;
  padding-left: 32px;
  padding-top: 32px;
  padding-right: 32px;
  padding-bottom: 72px;

  border-bottom-left-radius: 16px;
  border-bottom-right-radius: 16px;
  border-top: 1px solid #e9ecef;
`;

const Input = styled.input`
  padding: 12px;
  border-radius: 4px;
  border: 1px solid #dee2e6;
  width: 100%;
  outline: none;
  font-size: 18px;
  box-sizing: border-box;
`;

function TodoCreate(props) {
  let [입력값, 입력값변경] = useState('')
  
  return (
    <InsertFormPositioner>
      <InsertForm>
        <Input autoFocus placeholder="할 일을 입력하세요"
          onChange= { (e) => { 입력값변경(e.target.value )}}
        />
        <button onClick={
          (e)=> {props.dispatch({ type : 'CREATE', payload : {id:0, text : 입력값  }})
          e.preventDefault() // 새로고침 방지

          }} >추가</button>
      </InsertForm>
    </InsertFormPositioner>
  )
}

function state를props화(state) {
  return {
    state : state
  }
}

export default connect(state를props화)(TodoCreate);