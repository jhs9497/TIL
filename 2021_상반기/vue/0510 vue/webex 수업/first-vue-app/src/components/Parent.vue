<template>
  <div>
    <h1>Parent</h1>
    <p>From parent: {{ parentMessage }}</p>
    <Child @my-event="onMyEvent"/> <!--사용등록-->
    <Orphan/>
  </div>
</template>

<script>
import Child from './Child.vue' // 자식노드 불러오기
import Orphan from './Orphan.vue'

export default {
  name: 'Parent',
  components: {
    Child, // 자식노드 등록하기
    Orphan,
  },
  props: {
    parentMessage: String, 
  },
  methods: {
    onMyEvent: function() {
      console.log('자식에서 호출했어요!')
    },
  },
}
</script>

<style>

</style>