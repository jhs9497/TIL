import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
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
    }
  },
  actions: {
    createTodo: function (context, todoItem) {
      context.commit('CREATE_TODO', todoItem) // mutation (CREATE_TODO) 호출하기
    }
  },
  modules: {
  }
})
