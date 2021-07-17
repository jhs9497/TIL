function authUserReducer(state = false, action) {
  switch(action.type){
    case 'LOGIN':
      state = true
      return state
    case 'LOGOUT':
      state = false
      return state
      
    default:
      state = false
      return state
      
  }
}
export default authUserReducer;