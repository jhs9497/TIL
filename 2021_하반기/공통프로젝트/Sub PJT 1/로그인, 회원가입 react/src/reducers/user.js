let 유저정보 = [
  {
    username : '익명의 누군가',
    name: '',
    email:'',
  }
]

function userReducer (state = 유저정보, action) {
  if (action.type === 'SIGNUP') {

    // console.log('1번')
    // console.log(action[0].payload)
    // console.log('2번')
    // console.log(action.payload)
    // console.log('3번')

    let copy = [...state]
    copy.username = action.payload.username
    copy.name = action.payload.name
    copy.email = action.payload.email
    console.log(copy)
    return copy
  }

  return state
  
}
export default userReducer;