import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todoList: [],
  },
  getters: {
    getTodoList(state) {
      return state.todoList
    },
  },
  mutations: {
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
      // // 1. todoItem이 첫번째로 만나는 요소의 index를 가져옴
      // const index = state.todoList.indexOf(targetTodo)
      // // 2. 해당 인덱스 1개만 삭제하고 나머지 요소를 토대로 새로운 배열 생성
      // state.todoList.splice(index, 1) // index해당되는거 1개만 지우고 새로운 배열 생성

      state.todoList = state.todoList.map((todo) => {
        if (todo.id === targetTodo.id) {
          state.todoList.pop(targetTodo)
        }
        return todo
      })
    }
  },
  actions: {
  },
  modules: {
  }
})
