<template>
  <div class="search-bar">
    <input type="text" @keyup.enter="onKeywordEnter"> <!--enter를 치면 "함수"가 실행-->
  </div>
</template>

<script>
import axios from 'axios' // axios패키지에서 axios 꺼내기

const YOUTUBE_API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY  // youtube API KEY 변수화
const YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'SearchBar',
  methods: {
    async onKeywordEnter(event) {  // enter치면 넘어오는 input data?가 event에 담겨있음
      const keyword = event.target.value // keyword에 정의
      const config = {  // 넘기고 싶은거 정하기
        params: {
          part: 'snippet',
          type: 'video',
          q: keyword, // 검색어니깐 아까 받은 keyword 넣어주기
          key: YOUTUBE_API_KEY,
        },
      }

      const response = await axios.get(YOUTUBE_API_URL, config) // 유튜브 URL에 config와 함께 get요청 보내기
      const videoList = response.data.items
      this.$emit('on-keyword-enter', videoList) // 부모가 쓸 이름, 보낼 데이터 / 부모노드로 올리기
    },  // 위에서 enter치면 실행되는 함수 정의
  },
}
</script>

<style>
  .search-bar > input {  
    /* search-bar 안에 input태그에 스타일 적용 */
    width: 100%;
    padding: 0.5rem;
    font-size: 2rem;
  }
</style>