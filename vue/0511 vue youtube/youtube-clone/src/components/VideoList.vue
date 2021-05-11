<template>
  <div v-if="videoList.length"> <!--videoList가 비어있지 않을 때만 보이도록-->
    <VideoListItem
      v-for="(video, idx) in videoList" 
      :video="video"
      :key="idx"
    /> <!--반복문으로 보내주기-->
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
}
</script>

<style>

</style>