let 유저정보 = [
  {
    username : '익명의 누군가',
    name: '',
    email:'',
  }
]

function userReducer (state = 유저정보, action) {
  if (action.type === 'SIGNUP') {
    let copy = [...state]
    copy.username = action.payload.username
    copy.name = action.payload.name
    copy.email = action.payload.email
    return copy
  }

  return state
  
}
export default userReducer;