<template>
  <div id="app">
    <Profile v-if="isAuthenticated" /> <!--isAuthenticated에 따라서 profile이 보였다가 안보였다가-->
    <button @click="login">Login</button>
  </div>
</template>

<script>
import Profile from '@/components/Profile'

export default {
  name: 'App',
  components: {
    Profile
  },
  data() {
    return {}
  },
  methods: {
    login() {
      const token = 'asdf'
      // this.$store.commit('UPDATE_TOKEN', token)
      this.$store.dispatch('GET_TOKEN_FROM_SERVER', token)

      // django에 요청보내고 싶으면
      // axios.get('/login')
      // .then(res => {
      //   const token = res.data.token
      //   this.$store.dispatch('GET_TOKEN_FROM_SERVER', token)
      // })
    }
  },
  computed: {
    isAuthenticated() {
      return this.$store.getters.isAuthenticated 
      // this.store까지가 index.js의 store를 가리킴 + 
      // 그 안에 getters에서 isAuthenticated메소드를 가져옴
    },
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
