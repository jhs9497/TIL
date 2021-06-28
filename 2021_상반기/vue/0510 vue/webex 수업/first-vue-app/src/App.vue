<template>
  <div id="app">
    <Parent :parent-message="message"/> <!--3. 사용한다고 써준다!-->
  </div>
</template>

<script>
import Parent from './components/Parent.vue'  // 1. 컴포넌트를 불러온다.

export default {
  name: 'App', // 2. 앱등록을 해준다.
  components: {
    Parent, 
  },
  data: function() {
    return {
      message: '밥은 먹고 다니니?',
    }
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
