상근 : 영화 상세 페이지 + 추천페이지 UI 작성

현식 : 마이페이지완성, 리뷰페이지 거의 완성





오늘 할 것 : 장르별띄우기, 댓글작성기능, 추천페이지 기능 완성





로컬스토리지는 스트링만 저장할 수 있따

그러므로 배열이나 객체를 저장하고 싶을 땐 JSON.stringfy('') 를 통해 직렬화할것

```js
> localStorage.setItem('nums', JSON.stringify([1, 2, 3]))
undefined
> JSON.parse(localStorage.getItem('nums'))
[1, 2, 3]
```



data는 로컬스토리지를 쳐다보는건 아님! 처음에만 그렇고 따라서 함수에서 로컬스토리지에도 저장하고, data에도 저장해줘야함!