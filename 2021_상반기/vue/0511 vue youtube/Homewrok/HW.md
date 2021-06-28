## 1.

- F
- T
- F
  - native를 붙이지 않으면 custom events로 인식됨
  - ex) 자식 컴포넌트에서 this.$emit('click')형태로 사용하겠다는 의미가 됨

```vue
<correct>
<div @ click=""></div>

<videoList @click.native=""/>
    
    
<wrong>
<videoList @click=""/>
```



- F
  - props를 통해 자식 컴포넌트에게 데이터를 보내고 자식은 emit을 통해 부모에게 이벤트를 보낸다.



## 2.

하위 컴포넌트가 실수로 부모의 상태를 변경하여 앱의 데이터 흐름을 추론하기 더 어렵게 만드는 것을 방지할 수 있습니다.



## 3.

- this.$emit

- @addTodo="onAddTodo"

- onAddTodo(text) {

  console.log(text)

  }



