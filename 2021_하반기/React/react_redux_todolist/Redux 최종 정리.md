# Redux 최종 정리



참조 : https://react.vlpt.us/redux/07-implement-todos.html



## 액션(Action)

상태에 어떠한 변화가 필요하게 될 때, 우리는 액션이란 것을 발생시킨다. 이는, 하나의 객체로 표현되는데, 액션 객체는 다음과 같은 형식으로 이뤄져 있다.

다른 것들은 선택사항이지만 type은 반드시!! 들어가야 한다.

```react
{
    type : "ADD_TODO",
    data : {
        id : 0,
        text : "리덕스 배우기"
    }
}
```





## 액션 생성함수 (Action Creator)

액션을 만드는 함수이다. 파라미터를 받아와서 액션 객체 형태로 만들어준다. 보통 함수 앞에 export 키워드를 붙여서 자연스럽게 다른 파일에서 불러서 사용할 수 있도록 한다.

액션을 발생시킬 때 짧은 함수들은 굳이 액션생성함수를 정의해서 사용할 필요는 없다.

actions 폴더 안에 index.js를 만들어 한번에 모아서 보관한다! 마치 CSS처럼?

```react
export const increment = (nr) => {
  return {
    type: 'INCREMENT',
    payload: nr
  };
};
export const decrement = () => {
  return {
    type: 'DECREMENT'
  };
};
```



## 리듀서 (Reducer)

변화를 일으키는 함수이다. 리듀서는 두가지의 파라미터를 받아온다. 

reducers라는 폴더에 원하는 리듀서파일 모두 만든다음 index.js라는 파일 또 만들고 한번에 취합해서 export 해준다.

```react
const counterReducer = (state = 0, action) => {
  switch(action.type){
    case 'INCREMENT':     // 액션생성함수에서 정의한 변수명
      return state + action.payload;
    case 'DECREMENT':
      return state - 1;
    default:       // switch쓸꺼면 default 꼭 정해줘야함!
      return state;
  }
}
export default counterReducer;
```



## 스토어

리덕스에서는 한 애플리케이션 당 하나! 의 스토어를 만든다. 스토어 안에는, 현재의 앱 상태와, 리듀서가 들어가있고, 추가적으로 몇가지 내장함수들이 들어가있다 (일종의 독립된 데이터센터?)



## 디스패치 (dispatch)

액션을 발생 시키는 내장함수! dispatch(action)과 같은 형식으로 액션을 파라미터로 전달한다. 이렇게 호출을 하면 스토어는 리듀서 함수를 실행시켜 해당 액션을 처리하고 state를 업데이트한다.





















## 수정할 점

- input창 초기화가 안됨 ... useCallback사용하는게 아닌가 ?
- 추가된 todo에 고유한 id값을 쓰고 싶은데 잘 안되서 걍 랜덤 1000으로 했음 reducer안에서 for문이 돌아갈 수 없나 ?