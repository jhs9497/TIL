import data from '../data/todolistData.js'

let 기본state = data

function createReducer(state = 기본state, action) {
  switch(action.type){
    case 'CREATE':
      if (action.payload.text) {
        
        let copy = [...state]
  
        copy.push(action.payload) 
        console.log(copy)
        return copy
      } else {
        return state
      }

    case 'DELETE':
      let copy2 = [...state]
      console.log(action.payload, typeof(copy2))
      console.log(copy2)
      const filterd = copy2.filter((element) => element.id !== action.payload)
      // 삭제구현
      return filterd

    default:
      return state
  }
}
export default createReducer;