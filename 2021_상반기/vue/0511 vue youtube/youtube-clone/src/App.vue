<template>
  <div id="app">
    <header>
      <SearchBar
        @on-keyword-enter="onKeywordEnter" 
      /> <!--등록 3-->
    </header>

    <section>
      <VideoListItemDetail
        :video="video"
      />

      <VideoList 
        :videoList="videoList" 
        @on-select-video="onSelectVideo"
      />  <!--자식 노드인 VideoList에 보내주는거임! 왼쪽은 자식에서 쓸 이름, 오른쪽은 실제 이름-->
    </section>
    
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar.vue' // 등록 1
import VideoList from '@/components/VideoList.vue'
import VideoListItemDetail from '@/components/VideoListItemDetail.vue'

export default {
  name: 'App',
  components: {
    SearchBar, // 등록 2
    VideoList,
    VideoListItemDetail,
  },
  data() {
    return {
      videoList: [],
      video: null, // video를 우선 data로 저장을 하고 video detail로 보내준다!
    }
  },
  methods: {
    onKeywordEnter(videoList) { // SearchBar에서 보낸 videoList가 여기로 들어옴
      this.videoList = videoList // 위에 videoList array에 인자로 받은 videoList를 저장해준다.
    },
    onSelectVideo(video) {
      this.video = video
    },
  },
}
</script>

<style>
/* section과 header에 둘 다 스타일 주기 */
  section, header {  
    width: 80%;
    margin: 0 auto; 
    /* 위아래 0, 왼쪽오른쪽 auto ->가운데 정렬 */
    padding: 1rem 0;
  }

  section {
    display: flex;
  }
</style>
