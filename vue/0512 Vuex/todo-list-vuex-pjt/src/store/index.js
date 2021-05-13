import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
import createPersistedState from 'vuex-persistedstate' // web에 data저장을 위한 라이브러리 ?

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    todos: [
      {
        title: '할 일1',
        completed: false,
      },
      {
        title: '할 일2',
        completed: false,
      },
    ],
  },
  mutations: {
    CREATE_TODO: function (state, todoItem) { // 이름 왜 대문자 ? 걍 중요하니깐..
      // Action에서 보낸 todoItem 받아주고
      state.todos.push(todoItem) // state에 더해주기
    },
    DELETE_TODO: function (state, todoItem) {
      // 1. todoItem이 첫번째로 만나는 요소의 index를 가져옴
      const index = state.todos.indexOf(todoItem)
      // 2. 해당 인덱스 1개만 삭ㅈ0하고 나머지 요소를 토대로 새로운 배열 생성
      state.todos.splice(index, 1) // index해당되는거 1개만 지우고 새로운 배열 생성
    },
    UPDATE_TODO: function (state, todoItem) {
      state.todos = state.todos.map((todo) => { // state.todo를 돌면서
        if (todo === todoItem) { // todo랑 todoItem이랑 같으면
          return { ...todo, completed: !todo.completed } // ... 이거는 todo에서 completed만 효율적으로 바꾸고 싶을 때 사용 (덮어씌우는 느낌)
        }
        return todo
      })                                            
    }
  },
  actions: {
    createTodo: function (context, todoItem) {
      context.commit('CREATE_TODO', todoItem) // mutation (CREATE_TODO) 호출하기
    },
    deleteTodo: function ({ commit }, todoItem) {  // 위에랑 코드 같은거임
      commit('DELETE_TODO', todoItem)
    },
    updateTodo: function ({ commit }, todoItem) {
      commit('UPDATE_TODO', todoItem)
    },
  },
  getters: {
    completedTodosCount: function (state) {
      return state.todos.filter((todo) => {
        return todo.completed === true
      }).length // todo를 돌면서 todo.completed가 true인 애들의 길이를 return 하겠다 ( 갯수를 세겠다. )
    },
    uncompletedTodosCount: function (state) {
      return state.todos.filter((todo) => {
        return todo.completed === false
      }).length // todo를 돌면서 todo.completed가 true인 애들의 길이를 return 하겠다 ( 갯수를 세겠다. )
    },
  },
  modules: {
  }
})
