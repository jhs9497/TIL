<template>
  <div v-if="videoList.length"> <!--videoList가 비어있지 않을 때만 보이도록-->
    <VideoListItem
      v-for="video in videoList" 
      :video="video"
      :key="video.id.vidoId"
      @on-select-video="onSelectVideo" 
    /> <!--반복문으로 보내주기 key값은 고유한 값 console창에서 찾아서 넣어줘도 됨!-->
  </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem' // VideoListitem 불러오기

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  props: { // 부모노드에서 보내주는걸 props를 통해 받아주는것!
    videoList: Array, // type 적어주기
  },
  methods: {
    onSelectVideo(video) {
      this.$emit('on-select-video', video) // 여기는 중간노드기 때문에 video로 받은 것을 이름 그대로 app.vue로 올린다
    }
  },
}
</script>

<style>

</style>