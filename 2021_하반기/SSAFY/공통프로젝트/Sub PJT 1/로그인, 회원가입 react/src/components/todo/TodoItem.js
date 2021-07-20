/* eslint-disable */

import './TodoItem.css'
import { MdDelete } from 'react-icons/md';
import { useDispatch, useSelector } from 'react-redux'

function TodoItem () {

  const dispatch = useDispatch()
  const nowTodolist = useSelector(state => state.createReducer)


  return (
    <>
      {
        nowTodolist.map((value,i)=> {
          return (
            <div className="TodoItemBlock" key={i}>
              <div className="Text">{ value.text }</div>
              <div className="remove" onClick={()=>{ dispatch({ type : 'DELETE', payload: value.id}) }}>
                <MdDelete/>
              </div>
            </div>
          )
        })
      }   
    </>

  )
}


export default TodoItem;