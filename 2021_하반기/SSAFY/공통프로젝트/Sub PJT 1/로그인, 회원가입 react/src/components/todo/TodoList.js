import React from 'react';
import TodoItem from './TodoItem';
import { useSelector, useDispatch } from 'react-redux'
import { useEffect } from 'react';
import { useState } from 'react';
import './TodoList.css' 



function TodoList() {

  const dispatch = useDispatch()
  const alert열렸니 = useSelector(state => state.alertReducer)

  const [ID, ID변경] = useState('')

  useEffect(()=> {
    const localUser = localStorage.getItem('username')
    if (localUser) {
      ID변경(localUser)
    }
  },[])
  
  return (
    <div className='TodoListBlock'>
      <h1>{ID} 's TodoList</h1>
      <button onClick={()=>{ dispatch({type : 'ALERT'}) }}>눌러봐</button>
      {
        alert열렸니 === true
        ? <div className='MyAlert'></div>
        : null
      }
      <TodoItem></TodoItem>
    </div>
  );
}

export default TodoList;