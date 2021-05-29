## 1. Vue.js / MyPage comments 데이터 가져와서 추가 가공하기



```javascript
  // MyPage에서 내가 작성한 comments를 불러와야 하는데 내가 댓글 단 영화제목, 작성시간도 같이 띄워주고 싶다.
  // 그런데 comments 모델에는 댓글 작성한 movie_id만 있고 movie_title은 없는 상황
  created() {
    // 우선 로그인하면서 저장했던 store.state에서 내 user_id를 가져와서 내가 작성한 댓글의 정보를 가져온다.
    axios.get(`http://localhost:8000/api/v1/movie/${this.$store.state.id}/comment/user`)
      .then((res) => {
        // 그 데이터를 comments에 저장한다.
        this.comments = res.data
        // movie_list에 내가 댓글 단 movie_id를 먼저 넣어준다.
        let movie_list = []
        for (var i=0; i<this.comments.length; i++) {
          movie_list.push(this.comments[i].comment_movie)
        }
        // 댓글이 여러개면 movie_id가 여러개 일 수 있으므로
        // 중복을 없애고 movie_list를 다시 리스트화 하는 작업
        movie_list = [...new Set(movie_list)]

        const movie_info = []  // 내가 작성한 movie정보들을 담을 리스트
        // movie_list (movie_id의 리스트)를 돌면서 정보를 요청, 응답하며 movie_info에 저장해준다.
        movie_list.forEach(function(idx){
          movie_info.push(axios.get(`http://localhost:8000/api/v1/movie/${idx}/`))
        })

        // 2중 for문으로 comments 리스트에 맞는 영화제목 추가하기
        // for문 안에서 get.axios 보내면 비동기적 문제가 생김 그래서 Promise.all로 for문 아래를 시작해야함
        // 위 for문이 axios 모두 완료 되어야만 이하 코드가 실행된다는 느낌의 약속?
        Promise.all(movie_info)
        .then((res) => {
          for (let a=0; a<res.length; a++) {
            this.movies.push(res[a].data)
            
            for (let b=0; b<this.comments.length; b++) {
              // created_at도 뒤에 그냥 자르고 날짜만 보이도록 슬라이싱
              this.comments[b].created_at = this.comments[b].created_at.slice(0,10)
              // 만약 원하는 data를 찾았다면
              if (res[a].data.id === this.comments[b].comment_movie) {
              // comments에 'comment_title'이란 dict의 key느낌 친구 만들고 value 저장
                this.comments[b]['comment_title'] = res[a].data.title
              }
            }
          }
        })
      })
      .catch(error => console.log(error))
      
      
  // 이번 프로젝트를 하면서 비동기적이라는 특성 때문에 막히는 경우가 많았는데 위 코드 역시 비동기적인 상황때문에 논리상 문제가 	   없어보이는데 에러가 지속적으로 발생했었다. 굉장히 짧은 시간이지만 컴퓨터입장에서는 for문을 돌리고 axios를 보내놓고 받으      며 기다리고 있는데 또 다음 코드가 실행되는 상황에서 에러가 발생하는 것 같다. Promise.all이라는 친구를 이용하여 해결 할      수 있었다. 
```





## 2. Django / 영화 API 정보 가져오기

```python
def getMovie(request):
    # n을 변수로삼고 for문을 돌려서 충분한 양의 영화정보를 DB에 저장할 수 있도록 한다.
    for n in range(1, 20):
        movieURL = f'https://api.themoviedb.org/3/discover/movie?api_key={MYKEY}&language=ko-KR&page={str(n)}'
        # 스타트캠프 미세먼지 API 참조하며 가져오기,, 
        allMovie = requests.get(movieURL)
        # get 'results' 찾는데 시간이 좀 걸렸음 
        datas = allMovie.json().get('results')
        for data in datas:
            Movie.objects.get_or_create(
                # 원하는 친구들을 뽑아서 원하는 필드에 넣고
                movie_id = data.get('id'),
                title = data.get('original_title'),
                overview = data.get('overview'),
                release_date = data.get('release_date'),
                voteavg = data.get('vote_average'),
                # poster_path  + 하는 부분도 검색해서 알게됨
                poster_path = "https://image.tmdb.org/t/p/original"+ data.get('poster_path'),
            )
        
            # movie와 genre의 id끼리 M:N 모델을 수립하는 과정 
            # genre별 movie를 꺼내와야 하기 때문에 필요한 과정이다.
            # 해당 영화의 genre 저장해주고
            genreItems = data.get('genre_ids')
            # 지금 for문 내에 잡혀있는 movie_id의 정보들 가져온다음
            movie = Movie.objects.get(movie_id = data.get('id'))
            # 하나의 영화에 장르ID가 여러개 있기 때문에 for문을 돌려가며 추가해줘야한다
            for i in genreItems:
                p1 = get_object_or_404(Genre, pk=i)
                # M:N 필드에 추가
                movie.genres.add(p1)
    return


# restAPI도 오랜만이고 django도 오랜만이라서 처음에 조금 애먹었다. 특히 genre와 movie를 엮으면서 영화API를 DB에 저장하는 과정이 어려웠던 기억이 있다. 
```



## 느낀점

벌써 최종프로젝트라고 하니 감회가 새롭다. 그동안 이론과 짧은 프로젝트를 통해 익혔던 지식들을 재확인할 수 있어서 좋았다. 특히 내가 지금 보고 있는 인터넷 화면이 어떤 과정들을 밟으며 내 앞에 나타나는지 보다 더 명확히 그림이 그려진 FJT였던 것 같다. 또한 협업하는 방법, 내가 흥미있는 분야에 대해 조금씩 더 알아갈 수 있었던 매우 값진 시간이었다고 생각한다.