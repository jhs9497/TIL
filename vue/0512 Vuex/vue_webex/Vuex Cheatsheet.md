## Vuex Cheatsheet

### Vuex 기본요소

- state
- getters
- mutations
- actions



### 활용법

- state, getters => computed
  - state 사용법: `this.$store.state`
  - getters 사용법: `this.$store.getters.함수명`

- mutations, actions => methods

  - mutations 사용법: `this.$store.commit('문자열 형태의 함수명', 매개변수)`
  - actions 사용법: `this.$store.dispatch('mutation 함수명', 매개변수)`

  

