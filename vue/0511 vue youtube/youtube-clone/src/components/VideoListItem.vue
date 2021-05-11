<template>
  <div @click="onSelectVideo" class="video-list-item">
    <!-- {{ video.snippet.title }} -->
    <!-- {{ video.snippet.description }} -->
    <!-- {{ video.snippet.thumbnails.medium.url }} 이름이 너무 길어서 아래 computed로 변수재정의-->  
    <img v-bind:src="thumUrl" alt="">
    <h3>{{ videoTitle | unescape }}</h3> <!--밑에서 만든 필터함수 적용-->
    <p>{{ videoDesc }}</p>
  </div>
</template>

<script>
import _ from 'lodash' // npm한 lodash가져오고

export default {
  name: 'VideoListItem',
  props: {
    video: Object, // 형태는 객체형태
  },
  computed: {
    videoTitle() {
      return this.video.snippet.title
    },     // 변수를 깔끔하게 만들어주기
    videoDesc() {
      return this.video.snippet.description
    },
    thumUrl() {
      return this.video.snippet.thumbnails.medium.url
    },
  },
  filters: {
    unescape(rawText) {
      return _.unescape(rawText) // filter함수 만들고 위에 만든 변수에 적용시키면 됨! rawText라고 명명한 데이터가 들어오면
                                 // unescape시켜줌
    },
  },
  methods: {
    onSelectVideo() {
      this.$emit('on-select-video', this.video) // this.video가 가리키는 것은 props 안의 video!
    }, // click시 실행
  }
}
</script>

<style>
.video-list-item:hover { 
  /* hover 어떤 요소를 마우스로 갖다 대는 것! */
  cursor: pointer;
  background-color: #eee; 
  /* 갖다대면 커서를 바꿈! */
}
</style>