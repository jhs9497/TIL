import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todoList: [],
    errorMsg: '',
  },
  getters: {
    getTodoList(state) {
      return state.todoList
    },
  },
  mutations: {
    UPDATE_ERROR(state, errorMsg) {
      state.errorMsg = errorMsg
    },
    CREATE_TODO(state, newTodo) {
      state.todoList.push(newTodo)
    },
    UPDATE_TODO(state, targetTodo) {
      // 1. todoList에서 targetTodo를 찾고
      // 2. targetTodo의 completed 값을 바꿔준다.
      state.todoList = state.todoList.map((todo) => {
        if (todo.id === targetTodo.id) {
          todo.completed = !todo.completed
        }
        return todo
      })
    },
    DELETE_TODO(state, targetTodo) {
      // 1. targetTodo가 첫번째로 만나는 요소의 index를 가져옴
      const index = state.todoList.indexOf(targetTodo)
      // 2. 해당 인덱스 1개만 삭제하고 나머지 요소를 토대로 새로운 배열 생성
      state.todoList.splice(index, 1) // index해당되는거 1개만 지우고 새로운 배열 생성
      // 삭제한 요소를 return 함!
    }
  },
  actions: {
  },
  modules: {
  }
})
