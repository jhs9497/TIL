import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    // 사용할 데이터를 저장하는 곳
    token: null,
  },
  getters: {
    // computed처럼 state(데이터)를 변경하지 않고 활용할 때 사용
    isAuthenticated(state) { // 여기서의 state는 위에 state가 전체 들어온다고 생각하면됨
      const result = state.token ? true : false // stae.token이 참이면 앞에 treu / 거짓이면 뒤에 false를 쓴다.
      return result
    },

    },    
  mutations: {
    // state를 변경하는 함수를 정의하는 곳
    UPDATE_TOKEN(state, newToken) {
      state.token = newToken
    },
  },
  actions: {
    // state를 "비동기적으로" 변경할 때 사용하는
    // 함수를 정의하는 곳
    // 주의) 반드시 mutations를 통해 "간접적으로" 변경할 것
    GET_TOKEN_FROM_SERVER({ commit }, payload) {
      // context (객체) : state, commit, getters .. 등 다 들어있음!
      commit('UPDATE_TOKEN', payload)
    },
    
  },
  modules: {
  } // 지금은 필요없음 나중에 파일이 커지면 파일을 분리할때 사용
})
