<template>
  <div class="video-detail" v-if="video"> <!--초기값이 null이기 때문에 null인 친구의 videoUrl을 뽑으려다보니 에러가 발생한다.-->
    <div class="video-container">
      <iframe :src="videoUrl" frameborder="0">
      </iframe>
    </div>
  </div>
</template>

<script>
export default {
  name: 'VideoListItemDetail',
  props: {
    video: Object,
  },
  computed: {
    videoUrl() {
      const videoId = this.video.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    },
  },
}
</script>

<style>
.video-detail {
  width: 70%;
  padding: 1rem;
}

.video-container {
  position: relative;
  padding-top: 56.25%;
}

.video-container > iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
</style>