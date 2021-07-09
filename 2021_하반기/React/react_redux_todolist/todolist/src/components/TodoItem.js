import './TodoItem.css'
import { MdDelete } from 'react-icons/md';
import {connect} from 'react-redux'

function TodoItem ( props ) {
  return (
    <>
      {
        props.state.map((value,i)=> {
          return (
            <div className="TodoItemBlock">
              <div className="Text">{ value.text }</div>
              <div className="remove" onClick={()=>{ props.dispatch({ type : 'DELETE', payload: value.id}) }}>
                <MdDelete/>
              </div>
            </div>
          )
        })
      }   
    </>

  )
}

function state를props화(state) {
  return {
    state : state.createReducer,
    alert열렸니 : state.alertReducer,
  }
}

export default connect(state를props화)(TodoItem);