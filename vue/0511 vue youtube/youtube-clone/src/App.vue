<template>
  <div id="app">
    <SearchBar
      @on-keyword-enter="onKeywordEnter" 
    /> <!--등록 3-->
    <VideoList :videoList="videoList" />  <!--자식 노드인 VideoList에 보내주는거임! 왼쪽은 자식에서 쓸 이름, 오른쪽은 실제 이름-->
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar.vue' // 등록 1
import VideoList from '@/components/VideoList.vue'

export default {
  name: 'App',
  components: {
    SearchBar, // 등록 2
    VideoList,
  },
  data() {
    return {
      videoList: [],
    }
  },
  methods: {
    onKeywordEnter(videoList) { // SearchBar에서 보낸 videoList가 여기로 들어옴
      this.videoList = videoList // 위에 videoList array에 인자로 받은 videoList를 저장해준다.
      console.log('부모에서 찍음', videoList)
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
