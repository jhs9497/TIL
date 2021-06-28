/*
  [Object 요소 접근 연습]
  
	주어진 객체에서 items의 첫번째 아이템의 name을 result 변수에 할당하세요.
*/

const data = {
  id: 42,
  fullname: '광주',
  greeting: function () {
    // this: 메서드가 속한 객체의 속성을 참조할 때 사용
    console.log(`안녕, 난 지금 ${this.fullname}에 있어!`)
  },
  // 위를 ES6형식으로 축약하면
  // greeting() {
  //   console.log('안녕!')
  // }
  items: [
    {
      id: 1,
      name: 'foo',
    },
    {
      id: 2,
      name: 'bar',
    },
  ],
}
data.greeting()

const result = data.items[0].name // foo에 접근

const { fullname, id } = data // 구조 분해 할당
// console.log(name, id)



/*
[Object 축약 문법]

아래 변수들을 속성으로 가지는 Object를 축약문법을 활용하여 작성하세요.
*/

const username = 'hailey'
const contact = '010-1234-5678'
const personInfo = {
  username,
  contact,
}
console.log(personInfo)


/*
[Object Destructuring]

주어진 함수를 Object 축약 문법과, destructuring을 사용하여 재작성하세요.
*/

const users = [
  {
    name: 'hailey',
    contact: '010-1234-5678',
  },
  {
    name: 'paul',
    contact: '010-5678-1234',
  },
]

function saveUserData (users) {
  const userData = users.map((user, index) => { //
    return { 
      id: index, 
      name: user.name, //  
      contact: user.contact //
    }
  })

  return userData
}

console.log(saveUserData(users)) 

// 위가 원본 , 밑에 수정

const users = [
  {
    name: 'hailey',
    contact: '010-1234-5678',
  },
  {
    name: 'paul',
    contact: '010-5678-1234',
  },
]

function saveUserData (users) {
  const userData = users.map(( {name, contac}, index) => { //
    return { 
      id: index, 
      name, 
      contact,
    }
  })

  return userData
}

console.log(saveUserData(users)) 