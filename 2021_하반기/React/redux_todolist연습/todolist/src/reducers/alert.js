let 기본state = false

function alertReducer(state = 기본state, action) {
  switch(action.type){
    case 'ALERT':
      return !state
    default:
      return state
  }
}
export default alertReducer;