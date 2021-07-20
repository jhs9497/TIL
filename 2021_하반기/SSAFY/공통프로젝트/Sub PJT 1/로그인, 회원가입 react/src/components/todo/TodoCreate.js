import {useState} from 'react';
import './TodoCreate'
import { useDispatch } from 'react-redux';


function TodoCreate() {

  const dispatch = useDispatch()
  const [입력값, 입력값변경] = useState('')
  
  return (
    <div className='InsertFormPositioner'>
      <div className='InsertForm'>
        <input
          autoFocus placeholder="할 일을 입력하세요"
          value={입력값} // value까먹지말자
          onChange= { (e) => { 입력값변경(e.target.value )}}
        />
        <button onClick={
          (e)=> {dispatch({ type : 'CREATE', payload : {id: new Date().getTime(), text : 입력값  }})
          e.preventDefault() // 새로고침 방지
          입력값변경('')

          }} >추가</button>
      </div>
    </div>
  )
}

export default TodoCreate;