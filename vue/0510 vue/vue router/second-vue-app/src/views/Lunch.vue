<template>
  <div>
    <h1>Lunch Page</h1>

    추천받고 싶은 번호 개수를 입력해주세요:
    <input type="text" v-model="lottoNumber">
    <button @click="onClick">Lotto 페이지로 가기</button>
  </div>
</template>

<script>
export default {
  name: 'Lunch',
  data: function() {
    return {
      lottoNumber: 0,
    }
  },
  methods: {
    onClick: function() {
      this.$router.push(
        { name: 'Lotto',
          params: { lottoNumber: this.lottoNumber } 
        }
      )
    },
  },
}
</script>

<style>

</style>