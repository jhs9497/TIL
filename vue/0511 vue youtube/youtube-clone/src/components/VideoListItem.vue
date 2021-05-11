<template>
  <div>
    <!-- {{ video.snippet.title }} -->
    {{ videoTitle }}
    <!-- {{ video.snippet.description }} -->
    {{ videoDesc }}
    <!-- {{ video.snippet.thumbnails.medium.url }} 이름이 너무 길어서 아래 computed로 변수재정의-->  
    {{ thumUrl }}
  </div>
</template>

<script>

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
}
</script>

<style>

</style>