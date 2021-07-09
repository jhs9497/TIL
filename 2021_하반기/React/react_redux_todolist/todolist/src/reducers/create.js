import data from '.././data.js'

let 기본state = data

function createReducer(state = 기본state, action) {
  switch(action.type){
    case 'CREATE':
      let copy = [...state]
      const randomNum = Math.random() * 1000
      const randomId = Math.floor(randomNum)

      action.payload.id = randomId // 고유 id를 주기 위함인데 흠..

      copy.push(action.payload) 
      return copy

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