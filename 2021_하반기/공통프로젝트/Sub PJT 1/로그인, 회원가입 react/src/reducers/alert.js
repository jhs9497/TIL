let 기본state = false

function alertReducer(state = 기본state, action) {
  switch(action.type){
    case 'ALERT':
      console.log(!state)
      return !state
    default:
      console.log(state)
      return state
  }
}
export default alertReducer;