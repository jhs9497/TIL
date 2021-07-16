let 로그인 = 'X'

function authUserReducer(state = 로그인, action) {
  switch(action.type){
    case 'LOGIN':
      return 'O'
    case 'LOGOUT':
      return 'X'
    default:
      console.log(state)
      return state
  }
}
export default authUserReducer;