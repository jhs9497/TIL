<template>
  <div>
    <h1>Lotto Page</h1>
    <p>행운의 숫자: {{ luckyNumbers }} </p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'Lotto',
  data: function() {
    return {
      luckyNumbers: [],
    }
  },
  created() {
    // 1. params에 있는 숫자를 꺼내서
    const lottoNumber = this.$route.params.lottoNumber

    // 2. 랜덤한 숫자 뽑은 다음
    const randomNumbers = _.range(1, 46)
    const luckyNumbers = _.sampleSize(randomNumbers, lottoNumber)

    // 3. 화면에 출력
    this.luckyNumbers = luckyNumbers
  },
}
</script>

<style>

</style>